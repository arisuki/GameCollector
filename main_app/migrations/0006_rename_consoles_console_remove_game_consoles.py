# Generated by Django 4.2.1 on 2023-06-04 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_console_consoles_rename_console_game_consoles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consoles',
            new_name='Console',
        ),
        migrations.RemoveField(
            model_name='game',
            name='consoles',
        ),
    ]
