# Generated by Django 5.0.2 on 2024-03-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
