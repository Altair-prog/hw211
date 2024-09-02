# Generated by Django 5.0.7 on 2024-08-20 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_version_options_remove_version_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="version",
                to="catalog.product",
                verbose_name="Наименование продукта",
            ),
        ),
    ]
