# Generated by Django 4.2.5 on 2023-10-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physical', '0004_alter_asset_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemodel',
            name='image',
            field=models.ImageField(default='images/default-avatar.png', upload_to='src/img/models'),
        ),
        migrations.AlterField(
            model_name='disposeddevice',
            name='image',
            field=models.ImageField(default='images/default-avatar.png', upload_to='src/img/'),
        ),
        migrations.AlterField(
            model_name='hard_disk',
            name='image',
            field=models.ImageField(default='images/default-avatar.png', upload_to='src/img'),
        ),
    ]
