# Generated by Django 3.1.1 on 2020-12-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_laptop'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='name',
            field=models.CharField(default='null', max_length=30),
        ),
    ]