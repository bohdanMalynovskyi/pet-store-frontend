from celery import shared_task
from celery_singleton import Singleton
from django.core.mail import send_mail

from backend.settings import SITE_NAME


def send_order_email(email, subject, message):
    full_message = f"{message}\n\nЗ найкращими побажаннями,\n{SITE_NAME}"
    send_mail(
        f"{SITE_NAME} - {subject}",
        full_message,
        None,
        [email],
        fail_silently=False,
    )


@shared_task(base=Singleton)
def email_processing_order(order_id, email):
    message = f"Ваше замовлення #{order_id} зараз обробляється. Ми повідомимо вас, як тільки відправимо."
    send_order_email(email, "Ваше замовлення обробляється", message)


@shared_task(base=Singleton)
def email_cancelled_order(order_id, email):
    message = f"Шкодуємо повідомити вас, що ваше замовлення #{order_id} було скасовано."
    send_order_email(email, "Ваше замовлення скасовано", message)


@shared_task(base=Singleton)
def email_paid_order(order_id, email):
    message = f"Дякуємо за ваш платіж за замовлення #{order_id}. Ваше замовлення буде відправлено найближчим часом."
    send_order_email(email, "Ваше замовлення оплачено", message)


@shared_task(base=Singleton)
def email_finished_order(order_id, email):
    message = f"Ми раді повідомити вас, що ваше замовлення #{order_id} успішно виконане."
    send_order_email(email, "Ваше замовлення виконане", message)


@shared_task(base=Singleton)
def email_sent_order(order_id, email):
    message = f"Ваше замовлення #{order_id} відправлено. Ви отримаєте його найближчим часом."
    send_order_email(email, "Ваше замовлення відправлено", message)
