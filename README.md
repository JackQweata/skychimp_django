# Сервис Skychimp

Для удержания текущих клиентов зачастую используются вспомогательные или "прогревающие" рассылки для информирования и привлечения.
Cервис управления рассылками, администрирования и получения статистики.

# Настройки
1) заполнить .env:
   
  CACHE_ENABLED=True
  CACHE_LOCATION=redis://127.0.0.1:6379
  BD_NAME=****
  BD_USER=postgres
  BD_PASSWORD=****
  BD_PORT=5440
  EMAIL_HOST=****
  EMAIL_PASSWORD=****

3) выполнить команды:
  -) pip install -r requirements.txt
  -) python manage.py migrate
  -) python manage.py scu
  
