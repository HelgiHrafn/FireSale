# Generated by Django 4.0.4 on 2022-05-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_bio',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
