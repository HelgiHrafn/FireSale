# Generated by Django 4.0.4 on 2022-05-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_profile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_bio',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(max_length=9999, null=True),
        ),
    ]
