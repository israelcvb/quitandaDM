# Generated by Django 5.0.1 on 2024-01-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0003_alter_client_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="occurences",
            field=models.TextField(max_length=1024, null=True),
        ),
    ]
