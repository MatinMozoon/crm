from django.db import models


class EmailHistory(models.Model):
    """
    store result of celery
    """

    class Meta:
        verbose_name = 'تاریخچه ایمیل'
        verbose_name_plural = 'تاریخچه ایمیل ها'

    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='کاربر ارسال کننده')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    email_status = models.BooleanField(default=False, verbose_name='وضعیت ایمیل')
    email = models.CharField(max_length=100, verbose_name='ایمیل')
