# Generated by Django 4.2.11 on 2024-04-23 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollaborateRequest',
            new_name='ContactRequest',
        ),
    ]
