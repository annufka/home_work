# Generated by Django 3.1.5 on 2021-02-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefirst',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
