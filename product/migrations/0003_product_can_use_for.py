# Generated by Django 3.2.5 on 2021-07-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_organizationproduct_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='can_use_for',
            field=models.ManyToManyField(to='product.OrganizationProduct', verbose_name='قابل استفاده برای تولید محصول تولیدی'),
        ),
    ]
