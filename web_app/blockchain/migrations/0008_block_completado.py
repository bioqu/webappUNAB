# Generated by Django 5.1.dev20240419123637 on 2024-09-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchain", "0007_alter_block_cadena"),
    ]

    operations = [
        migrations.AddField(
            model_name="block",
            name="completado",
            field=models.BooleanField(default=False),
        ),
    ]
