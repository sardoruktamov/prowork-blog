# Generated by Django 3.2.4 on 2021-06-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtags',
            name='posts',
        ),
        migrations.AddField(
            model_name='hashtags',
            name='posts',
            field=models.ManyToManyField(to='app.Blog'),
        ),
    ]
