# Generated by Django 4.1 on 2024-01-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_remove_monthlyexpense_new_field_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="rajaswo",
            name="aarthik_barsa",
            field=models.CharField(default="80/81", max_length=20),
        ),
    ]
