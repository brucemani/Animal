# Generated by Django 3.2.3 on 2021-05-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PETApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='owner',
            field=models.CharField(default='', max_length=256),
        ),
    ]
