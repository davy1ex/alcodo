# Generated by Django 3.0 on 2019-12-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='Samara', max_length=64),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.CharField(default='anonymous-user.png', max_length=64),
        ),
    ]
