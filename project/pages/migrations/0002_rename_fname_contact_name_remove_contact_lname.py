# Generated by Django 5.0.3 on 2024-04-16 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
    ]
