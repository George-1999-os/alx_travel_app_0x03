INSTALLED_APPS = ['listings']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CELERY_BROKER_URL = 'amqp://localhost'
