# Generated by Django 4.1 on 2022-08-16 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_commands_config', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commandsbuttonsuser',
            name='parent_command',
        ),
        migrations.RemoveField(
            model_name='commandtext',
            name='parent_command',
        ),
        migrations.DeleteModel(
            name='CommandMedia',
        ),
        migrations.DeleteModel(
            name='CommandsButtonsUser',
        ),
        migrations.DeleteModel(
            name='CommandsConfig',
        ),
        migrations.DeleteModel(
            name='CommandText',
        ),
    ]