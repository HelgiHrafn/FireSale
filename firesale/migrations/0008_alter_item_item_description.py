# Generated by Django 4.0.4 on 2022-05-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firesale', '0007_alter_item_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
