# Generated by Django 4.0.4 on 2022-05-12 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_orderinfo_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.IntegerField(max_length=16, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvc',
            field=models.IntegerField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='exp_month',
            field=models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='exp_year',
            field=models.IntegerField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
