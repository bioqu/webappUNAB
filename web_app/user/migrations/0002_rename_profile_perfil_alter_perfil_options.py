# Generated by Django 5.1.dev20240419123637 on 2024-06-30 18:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Profile",
            new_name="Perfil",
        ),
        migrations.AlterModelOptions(
            name="perfil",
            options={"verbose_name": "Perfil", "verbose_name_plural": "Perfiles"},
        ),
    ]
