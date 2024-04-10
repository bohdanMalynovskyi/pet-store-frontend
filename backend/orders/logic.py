from django.db import transaction

from backend.settings import NP, SENDER_WAREHOUSE, CITY_SENDER, SENDER_REF, CONTACT_SENDER, SENDER_PHONE
from orders.models import OrderItem, Order


@transaction.atomic
def create_order_from_cart(cart, request):
    order = Order.objects.create(user=cart.user, unregistered_user=cart.unregistered_user, status='in_process',
                                 payment_type=request.data.get('payment_type'))

    total_price, total_weight = 0, 0

    for cart_item in cart.cart_items.all():
        discount_price = (cart_item.changeable_price.price - ((cart_item.changeable_price.price / 100) * cart_item.changeable_price.discount)) if cart_item.changeable_price else (
                cart_item.product.price - ((cart_item.product.price / 100) * cart_item.product.discount))

        OrderItem.objects.create(order=order, product=cart_item.product, fixed_price=discount_price,
                                 quantity=cart_item.quantity, changeable_price=cart_item.changeable_price)

        total_price += discount_price * cart_item.quantity
        total_weight += cart_item.changeable_price.weight if cart_item.changeable_price and cart_item.changeable_price.weight else cart_item.product.weight * cart_item.quantity

    user = order.unregistered_user if order.unregistered_user else order.user

    backward_delivery_data = [
        {"PayerType": "Recipient", "CargoType": "Money", "RedeliveryString": f'{total_price}'}] if request.data.get(
        'payment_type') == 'cash' else None

    response = NP.internet_document.save(
        sender_warehouse_index=SENDER_WAREHOUSE, recipient_warehouse_index=request.data.get('warehouse_index'),
        cargo_type='Cargo', seats_amount=1, payer_type='Recipient', payment_method='Cash', weight=total_weight,
        cost=total_price, service_type='WarehouseWarehouse', description='Зоотовари', sender=SENDER_REF,
        city_sender=CITY_SENDER, contact_sender=CONTACT_SENDER, senders_phone=SENDER_PHONE,
        recipients_phone=user.phone_number, city_recipient=request.data.get('city_ref'),
        recipient=user.counterparty_ref, contact_recipient=user.contact_person_ref,
        backward_delivery_data=backward_delivery_data
    )

    if response['success']:
        order.ref = response["data"][0]["Ref"]
        order.total_price = total_price
        order.save()
        cart.cart_items.all().delete()
    else:
        raise Exception(response['errors'])

    return order
