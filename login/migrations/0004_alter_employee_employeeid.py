# Generated by Django 4.0.4 on 2022-08-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmployeeID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
