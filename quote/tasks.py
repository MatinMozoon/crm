from time import sleep

from celery import Celery

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.html import strip_tags

from emailhistory import models
from organization.models import Organization


@shared_task
def email_quote_task(content, sender, receiver):
    sleep(1)
    try:
        send_mail('پیش فاکتور',
                  strip_tags(content),
                  settings.EMAIL_HOST_USER,
                  [receiver],
                  fail_silently=False)
        models.EmailHistory.objects.create(email_status=True, email=receiver, creator=get_user_model().objects.get(username=sender))
        return 'ایمیل ارسال شد.'
    except:
        models.EmailHistory.objects.create(email_status=False, email=receiver, creator=get_user_model().objects.get(username=sender))
        return 'ایمیل ارسال نشد.'
