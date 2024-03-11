# Generated by Django 4.1 on 2024-03-11 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Indicator",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="DebtData",
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
                ("year", models.IntegerField()),
                ("value", models.FloatField()),
                (
                    "debt_type",
                    models.CharField(
                        choices=[
                            ("central_government", "Central Government Debt"),
                            ("general_government", "General Government Debt"),
                            ("household", "Household Debt"),
                            ("non_financial_corporate", "Non Financial Corporate Debt"),
                            ("private", "Private debt"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="explorer_app.country",
                    ),
                ),
                (
                    "indicator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="explorer_app.indicator",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="debtdata",
            constraint=models.UniqueConstraint(
                fields=("country", "indicator", "year", "debt_type"),
                name="unique_debt_record",
            ),
        ),
    ]
