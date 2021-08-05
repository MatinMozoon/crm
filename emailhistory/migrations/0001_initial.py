# Generated by Django 3.2.5 on 2021-08-05 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('email_status', models.BooleanField(default=True, verbose_name='وضعیت ایمیل')),
                ('email', models.CharField(max_length=100, verbose_name='ایمیل')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ارسال کننده')),
            ],
            options={
                'verbose_name': 'تاریخچه ایمیل',
                'verbose_name_plural': 'تاریخچه ایمیل ها',
            },
        ),
    ]
