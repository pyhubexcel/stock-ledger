# Generated by Django 3.2 on 2022-06-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_ledger_models', '0004_auto_20220614_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='UPDATE_DATETIME',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
