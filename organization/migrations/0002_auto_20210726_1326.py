# Generated by Django 3.2.5 on 2021-07-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(error_messages={'unique': 'This email has already been registered.'}, max_length=100, unique=True, verbose_name='نام سازمان'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='number_of_employees',
            field=models.PositiveIntegerField(verbose_name='تعداد کارمندان'),
        ),
    ]