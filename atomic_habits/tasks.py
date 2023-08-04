from celery import shared_task
from celery.bin.result import result


@shared_task
def my_async_task(arg1, arg2):
    # Ваш код задачи
    return result
