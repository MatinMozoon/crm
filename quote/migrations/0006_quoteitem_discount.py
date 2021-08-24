# Generated by Django 3.2.5 on 2021-08-23 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_remove_quoteitem_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteitem',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف'),
        ),
    ]