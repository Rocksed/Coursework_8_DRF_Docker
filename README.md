Atomic Habits API

Данный проект представляет собой API для управления привычками.

Установка и настройка

    Клонируйте репозиторий:

bash

git clone https://github.com/your-username/atomic-habits-api.git

    Создайте и активируйте виртуальное окружение:

bash

cd atomic-habits-api
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

    Установите зависимости:

bash

pip install -r requirements.txt

    Создайте файл .env и заполните необходимыми данными:

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

YOUR_BOT_TOKEN=

    Примените миграции:

bash

python manage.py migrate

    Запустите сервер разработки:

bash

python manage.py runserver

Теперь ваш проект готов к использованию! Для более подробной информации о доступных API и эндпоинтах обратитесь к документации.


