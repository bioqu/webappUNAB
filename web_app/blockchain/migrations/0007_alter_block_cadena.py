# Generated by Django 5.1.dev20240419123637 on 2024-09-02 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchain", "0006_block_cadena"),
    ]

    operations = [
        migrations.AlterField(
            model_name="block",
            name="cadena",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bloques",
                to="blockchain.cadena",
            ),
        ),
    ]
