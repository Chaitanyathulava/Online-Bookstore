# Generated by Django 5.0.2 on 2024-04-26 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0009_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='message',
            new_name='textarea',
        ),
    ]
