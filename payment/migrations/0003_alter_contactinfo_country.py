# Generated by Django 4.0.4 on 2022-05-13 10:26

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_contactinfo_country_alter_payment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
