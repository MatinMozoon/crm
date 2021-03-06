# Generated by Django 3.2.5 on 2021-08-08 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0005_alter_organization_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='توضیحات')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('slug', models.SlugField(unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ثبت کننده')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.organization', verbose_name='سازمان')),
            ],
            options={
                'verbose_name': 'پیگیری',
                'verbose_name_plural': 'پیگیری ها',
            },
        ),
    ]
