from celery.utils.time import timezone
from django.utils.datetime_safe import datetime
from telegram import Bot
from celery import shared_task
from atomic_habits.models import Habit
from telegram_bot import TELEGRAM_BOT_TOKEN


@shared_task
def send_notifications():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)  # Получите токен бота

    now = datetime.now(timezone.utc)
    habits_to_notify = Habit.objects.filter(notification_datetime__lte=now, is_notified=False)

    for habit in habits_to_notify:
        # Отправьте уведомление пользователю через телеграм-бот
        chat_id = habit.user.telegram_chat_id  # Получите chat_id пользователя из модели Habit
        message = "Напоминание: " + habit.title  # Сообщение для уведомления

        bot.send_message(chat_id=chat_id, text=message)

        # Пометьте привычку как уведомленную, чтобы избежать повторных уведомлений
        habit.is_notified = True
        habit.save()
