# Generated by Django 5.0.1 on 2024-01-11 15:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0004_client_occurences"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="occurences",
            new_name="occurrences",
        ),
    ]
