# test_task_EORA

### Запуск бота:
- python3 tg_bot/main.py

### Запуск API для общения с ботом:
- sudo docker-compose up

##### Эндпоинты для API:
- api/get-login-code/ - получение кода для входа в Телеграм
- api/login/ - вход в Телеграм
- api/send-message/ - отправка сообщения боту :cat2: or :bread: (@EoraTaskBot)
Более подробная информация в документации (файл openapi.json)
##### База данных:
- модель Message: id - первичный ключ, user_id - id юзера, от имеи которого отправляется сообщение, 
message - текст сообщения

