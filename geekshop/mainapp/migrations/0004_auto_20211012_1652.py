# Generated by Django 3.2.8 on 2021-10-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='adress',
            field=models.CharField(max_length=64, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=32, verbose_name='эл. почта'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.PositiveIntegerField(unique=True, verbose_name='телефон'),
        ),
    ]
