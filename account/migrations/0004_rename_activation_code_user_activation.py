# Generated by Django 4.0 on 2021-12-28 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_activation_user_activation_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='activation_code',
            new_name='activation',
        ),
    ]