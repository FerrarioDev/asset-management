# Generated by Django 4.2.5 on 2023-10-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='location',
            field=models.CharField(default='Office 1', max_length=255),
            preserve_default=False,
        ),
    ]