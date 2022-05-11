# Generated by Django 4.0.4 on 2022-05-09 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firesale', '0003_itemcategory_remove_item_item_image_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_name', models.CharField(max_length=50)),
                ('street_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('post_code', models.IntegerField()),
                ('payment_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]