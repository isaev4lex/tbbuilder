# Generated by Django 4.1 on 2022-08-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_step_messaging_config', '0011_stepmessagingconfig_last_bot_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepmessagingconfig',
            name='last_bot_message',
            field=models.TextField(default='', max_length=120, verbose_name='Enter the last message for user from bot, for completing step messaging'),
        ),
    ]
