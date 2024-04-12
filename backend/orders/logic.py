from django.db import transaction
from backend.settings import NP, SENDER_WAREHOUSE, CITY_SENDER, SENDER_REF, CONTACT_SENDER, SENDER_PHONE
from orders.models import OrderItem, Order
from users.models import User


@transaction.atomic
def create_order_from_cart(cart, request):
    counterparty_ref, contact_person_ref = _get_counterparty_info(cart, request)
    order = _create_order(cart, request, counterparty_ref, contact_person_ref)
    _create_order_items(order, cart)
    _process_delivery(order, request, cart)
    return order


def _get_counterparty_info(cart, request):
    if not cart.user:
        required_fields = ['first_name', 'last_name', 'phone']
        for field in required_fields:
            if not request.data.get(field):
                raise Exception({field: ['This field is required.']})

        response = NP.counterparty.save(request.data.get('first_name'), request.data.get('second_name', ''),
                                        request.data.get('last_name'), request.data.get('phone'), '', 'PrivatePerson',
                                        '', 'Recipient', '')
        if response['success']:
            ref = response["data"][0]["Ref"]
            contact_person_ref = response["data"][0]["ContactPerson"]['data'][0]["Ref"]
            return ref, contact_person_ref
        else:
            print(response)
            raise Exception(response['errors'])
    return None, None


def _create_order(cart, request, counterparty_ref, contact_person_ref):
    return Order.objects.create(
        user=cart.user,
        status='in_process',
        payment_type=request.data.get('payment_type'),
        counterparty_ref=counterparty_ref,
        contact_person_ref=contact_person_ref
    )


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
    return total_price, total_weight


def _process_delivery(order, request, cart):
    total_price, total_weight = _create_order_items(order, cart)
    refs = order.user if order.user else order

    backward_delivery_data = [
        {"PayerType": "Recipient", "CargoType": "Money", "RedeliveryString": f'{total_price}'}] if request.data.get(
        'payment_type') == 'cash' else None

    response = NP.internet_document.save(
        sender_warehouse_index=SENDER_WAREHOUSE, recipient_warehouse_index=request.data.get('warehouse_index'),
        cargo_type='Cargo', seats_amount=1, payer_type='Recipient', payment_method='Cash', weight=total_weight,
        cost=total_price, service_type='WarehouseWarehouse', description='Зоотовари', sender=SENDER_REF,
        city_sender=CITY_SENDER, contact_sender=CONTACT_SENDER, senders_phone=SENDER_PHONE,
        recipients_phone=refs.phone_number if isinstance(refs, User) else request.data.get('phone'),
        city_recipient=request.data.get('city_ref'), backward_delivery_data=backward_delivery_data,
        recipient=refs.counterparty_ref, contact_recipient=refs.contact_person_ref
    )

    if response['success']:
        order.document_ref = response["data"][0]["Ref"]
        order.total_price = total_price
        order.save()
        cart.cart_items.all().delete()
    else:
        raise Exception(response['errors'])
