# Generated by Django 3.2.5 on 2021-07-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_auto_20210703_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
    ]
