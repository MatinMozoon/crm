# Generated by Django 3.2.5 on 2021-08-06 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_remove_quoteitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteitem',
            name='discount',
        ),
    ]