from datetime import datetime, timedelta
from pytz import timezone

from celery import shared_task
from celery.schedules import crontab
from drf_api_logger.models import APILogsModel
from celery.utils.log import get_task_logger
from celery_singleton import Singleton

from celery_app import app
from users.models import Cart, FeaturedProducts

logger = get_task_logger(__name__)


kiev_tz = timezone('Europe/Kiev')


@shared_task(base=Singleton)
def set_interact(cart_id=None, featured_id=None):
    if cart_id:
        obj = Cart.objects.get(pk=cart_id)
    else:
        obj = FeaturedProducts.objects.get(pk=featured_id)
    obj.last_updated = datetime.now(kiev_tz)
    obj.save()


@app.task
@shared_task(base=Singleton)
def delete_old_carts():
    one_week_ago = datetime.now(kiev_tz) - timedelta(weeks=1)

    old_cart = Cart.objects.filter(hash_code__isnull=False, last_interact__lte=one_week_ago)
    old_cart.delete()
    logger.info("Old carts have been deleted")


@app.task
@shared_task(base=Singleton)
def delete_old_featured():
    one_week_ago = datetime.now(kiev_tz) - timedelta(weeks=1)

    old_featured = FeaturedProducts.objects.filter(hash_code__isnull=False, last_interact__lte=one_week_ago)
    old_featured.delete()
    logger.info("Old featured have been deleted")


@app.task
@shared_task(base=Singleton)
def delete_old_logs():
    one_week_ago = datetime.now(kiev_tz) - timedelta(weeks=1)

    old_logs = APILogsModel.objects.filter(added_on__lt=one_week_ago)
    old_logs.delete()

    logger.info("Old logs have been deleted")


app.conf.timezone = 'Europe/Kiev'

app.conf.beat_schedule = {
    'delete_old_carts': {
        'task': 'users.tasks.delete_old_carts',
        'schedule': crontab(minute='0', hour='1')
    },
    'delete_old_featured': {
        'task': 'users.tasks.delete_old_featured',
        'schedule': crontab(minute='0', hour='2')
    },
    'delete_old_logs': {
        'task': 'users.tasks.delete_old_featured',
        'schedule': crontab(minute='0', hour='3')
    }
}
