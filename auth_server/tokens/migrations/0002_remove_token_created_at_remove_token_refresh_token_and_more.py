# Generated by Django 5.0.4 on 2024-04-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='token',
            name='refresh_token',
        ),
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.CharField(max_length=2048),
        ),
    ]
