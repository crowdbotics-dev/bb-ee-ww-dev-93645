# Generated by Django 2.2.28 on 2023-06-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230622_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='afsd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='asdf',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dghj',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
