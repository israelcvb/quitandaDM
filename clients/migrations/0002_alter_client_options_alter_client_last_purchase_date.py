# Generated by Django 5.0.1 on 2024-01-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "cliente"},
        ),
        migrations.AlterField(
            model_name="client",
            name="last_purchase_date",
            field=models.DateField(null=True, verbose_name="data da última compra"),
        ),
    ]
