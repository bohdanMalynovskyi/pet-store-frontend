from decimal import Decimal

from cloudipsp import Checkout
from django.db import transaction, IntegrityError
from django.urls import reverse

from backend.settings import NP, SENDER_WAREHOUSE, CITY_SENDER, SENDER_REF, CONTACT_SENDER, SENDER_PHONE, FONDY
from orders.models import OrderItem, Order
from users.models import User
from .tasks import email_processing_order


@transaction.atomic
def create_order_from_cart(cart, request):
    payment_type = request.data.get('payment_type')
    email = request.data.get('email')
    counterparty_ref, contact_person_ref = _get_counterparty_info(cart, request)
    order = _create_order(cart, payment_type, counterparty_ref, contact_person_ref, email)
    total_weight = _create_order_items(order, cart)
    checkout_url = None
    if payment_type == 'cash':
        process_delivery(order, request, total_weight)
    elif payment_type == 'online':
        checkout_url = process_payment(order, request, total_weight)
    return order, checkout_url


def _get_counterparty_info(cart, request):
    if not cart.user:
        required_fields = ['email', 'first_name', 'last_name', 'phone']
        for field in required_fields:
            if not request.data.get(field):
                raise Exception({field: ['This field is required.']})

        response = NP.counterparty.save(request.data.get('first_name'), request.data.get('second_name', ''),
                                        request.data.get('last_name'), request.data.get('phone'),
                                        request.data.get('email'), 'PrivatePerson', '', 'Recipient', '')
        if response['success']:
            ref = response["data"][0]["Ref"]
            contact_person_ref = response["data"][0]["ContactPerson"]['data'][0]["Ref"]
            return ref, contact_person_ref
        else:
            raise Exception(response['errors'])
    return None, None


def _create_order(cart, payment_type, counterparty_ref, contact_person_ref, email):
    order = Order.objects.create(
        user=cart.user,
        email=email,
        status='in_process' if payment_type == 'cash' else 'waiting_for_payment' if payment_type == 'online' else None,
        payment_type=payment_type,
        counterparty_ref=counterparty_ref,
        contact_person_ref=contact_person_ref
    )
    email_processing_order.delay(order_id=order.id, email=email if email else order.user.email)
    return order


def _create_order_items(order, cart):
    total_price, total_weight = 0, 0
    for cart_item in cart.cart_items.all():
        discount_price = (cart_item.changeable_price.price - ((cart_item.changeable_price.price / 100) * cart_item.changeable_price.discount)) if cart_item.changeable_price else (
                cart_item.product.price - ((cart_item.product.price / 100) * cart_item.product.discount))

        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            fixed_price=discount_price,
            quantity=cart_item.quantity,
            changeable_price=cart_item.changeable_price
        )

        total_price += discount_price * cart_item.quantity
        total_weight += cart_item.changeable_price.weight if cart_item.changeable_price and cart_item.changeable_price.weight else cart_item.product.weight * cart_item.quantity
        try:
            cart_item.product.quantity -= cart_item.quantity
            cart_item.product.save()
        except IntegrityError:
            raise IntegrityError('Store dont have enough products')
    order.total_price = total_price
    order.save()
    cart.cart_items.all().delete()
    return total_weight


def process_payment(order, request, total_weight):
    amount = str(order.total_price).replace('.', '')
    # TODO: ADD 'order_id': order.id
    ck = Checkout(api=FONDY).url(
        {'currency': 'UAH', 'amount': int(amount), 'order_desc': 'Зоотовари',
         'lang': 'uk', 'server_callback_url': reverse('approve_payment'), 'lifetime': 18000,
         'merchant_data': {'warehouse_index': request.data.get('warehouse_index'),
                           'city_ref': request.data.get('city_ref'), 'phone': request.data.get('phone'),
                           'total_weight': str(total_weight)}})
    return ck.get('checkout_url')


def process_delivery(order, request=None, total_weight=None, merchant_data=None):
    refs = order.user if order.user else order

    backward_delivery_data = [
        {"PayerType": "Recipient", "CargoType": "Money",
         "RedeliveryString": f'{order.total_price}'}] if not merchant_data else None

    response = NP.internet_document.save(
        sender_warehouse_index=SENDER_WAREHOUSE,
        recipient_warehouse_index=request.data.get('warehouse_index') if not merchant_data else merchant_data[
            'warehouse_index'],
        cargo_type='Cargo', seats_amount=1, payer_type='Recipient', payment_method='Cash',
        weight=total_weight if total_weight else Decimal(merchant_data['total_weight']),
        cost=order.total_price, service_type='WarehouseWarehouse', description='Зоотовари', sender=SENDER_REF,
        city_sender=CITY_SENDER, contact_sender=CONTACT_SENDER, senders_phone=SENDER_PHONE,
        recipients_phone=refs.phone_number if isinstance(refs, User) else request.data.get(
            'phone') if not merchant_data else merchant_data['phone'],
        city_recipient=request.data.get('city_ref') if not merchant_data else merchant_data['city_ref'],
        recipient=refs.counterparty_ref,
        backward_delivery_data=backward_delivery_data, contact_recipient=refs.contact_person_ref
    )

    if response['success']:
        order.document_ref = response["data"][0]["Ref"]
        order.save()
    else:
        raise Exception(response['errors'])
