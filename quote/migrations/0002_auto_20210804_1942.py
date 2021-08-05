# Generated by Django 3.2.5 on 2021-08-04 19:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='discount',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='quoteitem',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_item', to='quote.quote', verbose_name='پیش فاکتور'),
        ),
    ]
