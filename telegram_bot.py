import logging
import os

from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Установите ваш токен
TELEGRAM_BOT_TOKEN = os.getenv('YOUR_BOT_TOKEN')

# Настройте логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Hello! I am your bot.')


# Создайте бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)
updater = Updater(bot=bot, use_context=True)

# Добавьте обработчик команды /start
updater.dispatcher.add_handler(CommandHandler('start', start))

# Запустите бота
updater.start_polling()

# Остановка бота при получении сигнала выхода
updater.idle()
