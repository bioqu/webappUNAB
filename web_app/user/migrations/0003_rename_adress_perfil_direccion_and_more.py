# Generated by Django 5.1.dev20240419123637 on 2024-06-30 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_rename_profile_perfil_alter_perfil_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="perfil",
            old_name="adress",
            new_name="Direccion",
        ),
        migrations.RenameField(
            model_name="perfil",
            old_name="image",
            new_name="Imagen",
        ),
        migrations.RenameField(
            model_name="perfil",
            old_name="staff",
            new_name="Staff",
        ),
        migrations.RenameField(
            model_name="perfil",
            old_name="phone",
            new_name="Telefono",
        ),
    ]
