# Generated by Django 3.2.3 on 2021-05-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PETApp', '0002_petmodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petmodel',
            name='petImage',
            field=models.ImageField(upload_to='images'),
        ),
    ]
