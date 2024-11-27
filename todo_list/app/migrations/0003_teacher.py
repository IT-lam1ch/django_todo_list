# Generated by Django 5.1.2 on 2024-11-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_todo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("subject", models.CharField(max_length=100)),
            ],
        ),
    ]
