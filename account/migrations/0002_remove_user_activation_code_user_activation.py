# Generated by Django 4.0 on 2021-12-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_code',
        ),
        migrations.AddField(
            model_name='user',
            name='activation',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
