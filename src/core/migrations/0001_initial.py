# Generated by Django 2.2.19 on 2021-02-21 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GiftCardInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("redeemable_code", models.CharField(max_length=50)),
                ("denomination", models.PositiveIntegerField()),
                ("pin", models.CharField(max_length=100)),
                ("source", models.CharField(max_length=100)),
                (
                    "date_of_purchase",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("used_on", models.DateTimeField(null=True)),
                ("used_by", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
