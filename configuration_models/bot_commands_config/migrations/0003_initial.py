# Generated by Django 4.1 on 2022-08-16 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot_commands_config', '0002_remove_commandsbuttonsuser_parent_command_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandsConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name="Command ( Without '/' )")),
                ('text', models.TextField(null=True, verbose_name='Enter your text message for replying')),
                ('send_first', models.CharField(choices=[('text', 'Text Message'), ('media', 'Media Message')], default='text', max_length=20, verbose_name='Send first')),
            ],
            options={
                'verbose_name': 'Command replying configuration',
                'verbose_name_plural': 'Commands replying configurations',
            },
        ),
        migrations.CreateModel(
            name='CommandText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Enter your additional text for message')),
                ('parent_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_commands_config.commandsconfig')),
            ],
            options={
                'verbose_name': 'Additional Text Message for Reply',
                'verbose_name_plural': 'Additional Text Messages for Reply',
            },
        ),
        migrations.CreateModel(
            name='CommandsButtonsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_1', models.CharField(max_length=21, verbose_name='Button №1 text')),
                ('button_2', models.CharField(blank=True, max_length=21, verbose_name='Button №2 text')),
                ('button_3', models.CharField(blank=True, max_length=21, verbose_name='Button №3 text')),
                ('parent_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_commands_config.commandsconfig')),
            ],
            options={
                'verbose_name': 'User button',
                'verbose_name_plural': 'User buttons',
            },
        ),
        migrations.CreateModel(
            name='CommandMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True, verbose_name='Caption')),
                ('media_file', models.FileField(upload_to='bot-media-files', verbose_name='Add your media file for message')),
                ('parent_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_commands_config.commandsconfig')),
            ],
            options={
                'verbose_name': 'Media Message for Reply',
                'verbose_name_plural': 'Media Messages for Reply',
            },
        ),
    ]
