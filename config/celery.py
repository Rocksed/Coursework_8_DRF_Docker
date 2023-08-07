from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Установите переменную окружения DJANGO_SETTINGS_MODULE, указывающую на ваш файл settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('Coursework_7_DRF')

# Импортируйте настройки Django для использования в настройках Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживайте и регистрируйте задачи в приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
