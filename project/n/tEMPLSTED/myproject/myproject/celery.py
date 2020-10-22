import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
app.conf.timezone = 'UTC'




app.conf.beat_schedule = {
    'checking_user_every_5mins': {
        'task': 'users.tasks.check_if_user_has_expired',
        'schedule': crontab(),
        #'args': (16, 16),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },

        'send_mail_to_expired_users': {
            'task': 'users.tasks.get_expired_users_and_send_mail',
            'schedule': crontab(),
        },

        'get_paid_users_and_send_mail': {
            'task': 'users.tasks.get_paid_users_and_send_mail',
            'schedule': crontab(),
        }

}


app.conf.timezone = 'UTC'