# Generated by Django 4.0.4 on 2022-08-21 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Phone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='[0-9]{10}*')]),
        ),
    ]