# Generated by Django 4.1 on 2022-08-10 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("simple_excel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParentModel",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TestModel",
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
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("description", models.TextField(verbose_name="description")),
                ("age", models.IntegerField()),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="simple_excel.parentmodel",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="SiteInfo",
        ),
    ]
