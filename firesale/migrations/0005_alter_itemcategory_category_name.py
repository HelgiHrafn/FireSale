# Generated by Django 4.0.4 on 2022-05-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firesale', '0004_item_item_category_alter_itemcategory_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategory',
            name='category_name',
            field=models.CharField(max_length=255),
        ),
    ]