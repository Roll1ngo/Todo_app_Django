# Generated by Django 5.0.2 on 2024-03-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=260)),
                ("completed", models.BooleanField(default=False)),
                ("published", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-published"],
            },
        ),
    ]
