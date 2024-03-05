from datetime import datetime, timedelta

from celery import shared_task
from celery.schedules import crontab

from celery.utils.log import get_task_logger
from celery_singleton import Singleton

from celery_app import app
from users.models import Cart, FeaturedProducts

logger = get_task_logger(__name__)


@shared_task(base=Singleton)
def set_interact(cart_id=None, featured_id=None):
    if cart_id:
        obj = Cart.objects.get(pk=cart_id)
    else:
        obj = FeaturedProducts.objects.get(pk=featured_id)
    obj.last_updated = datetime.now()
    obj.save()


@app.task
@shared_task(base=Singleton)
def delete_old_carts():
    one_week_ago = datetime.now() - timedelta(weeks=1)

    for cart in Cart.objects.filter(hash_code__isnull=False):
        if cart.last_interact < one_week_ago:
            cart.delete()
    logger.info("Old carts have been deleted")


@app.task
@shared_task(base=Singleton)
def delete_old_featured():
    one_week_ago = datetime.now() - timedelta(weeks=1)

    for featured in FeaturedProducts.objects.filter(hash_code__isnull=False):
        if featured.last_interact < one_week_ago:
            featured.delete()
    logger.info("Old featured have been deleted")


app.conf.beat_schedule = {
    'delete_old_carts': {
        'task': 'users.tasks.delete_old_carts',
        'schedule': crontab(minute='0', hour='2')
    },
    'delete_old_featured': {
        'task': 'users.tasks.delete_old_featured',
        'schedule': crontab(minute='0', hour='2')
    }
}
