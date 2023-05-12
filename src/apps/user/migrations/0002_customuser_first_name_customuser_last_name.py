# Generated by Django 4.2.1 on 2023-05-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия'),
        ),
    ]