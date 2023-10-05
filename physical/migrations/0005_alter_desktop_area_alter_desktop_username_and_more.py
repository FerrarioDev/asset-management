# Generated by Django 4.2.5 on 2023-10-05 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_area_area_name_alter_user_username'),
        ('physical', '0004_alter_desktop_area_alter_desktop_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.area'),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.area'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
