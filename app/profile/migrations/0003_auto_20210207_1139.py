# Generated by Django 3.1.5 on 2021-02-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_profilefirst_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilefirst',
            name='balance',
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
