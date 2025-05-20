# Телеграм бот для цветочного магазина Flowers-market-bot

## 🛠️ Технологии  
- **Python 3.12**  
- **Aiogram 3.x** (асинхронный фреймворк для Telegram Bot API)  
- **SQLAlchemy** (ORM для работы с базой данных)  
- **MySQL** (или другая СУБД)

## 🚀 Запуск
1. Установите зависимости:  
	```bash
	pip install -r requirements.txt

2. Создайте два файла .env (bot.env и database.env) в папке src/config:
	Структура файла bot.env:
		BOT_TOKEN='Ваш токен'
	Структура файла database.env:
		DB_USER = 'Ваши данные для подключения'
		DB_PASS = 'Ваши данные для подключения'
		DB_HOST = 'Ваши данные для подключения'
		DB_NAME = 'Ваши данные для подключения'

3. Запустите бота:
	python -m src.bot.bot_base

## 📄 Лицензия
Проект распространяется под лицензией MIT.