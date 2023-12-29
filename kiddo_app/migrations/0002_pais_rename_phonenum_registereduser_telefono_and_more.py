# Generated by Django 5.0 on 2023-12-29 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kiddo_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pais",
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
                ("nombre", models.CharField(max_length=100)),
            ],
            options={"verbose_name": "País", "verbose_name_plural": "Países",},
        ),
        migrations.RenameField(
            model_name="registereduser", old_name="phoneNum", new_name="telefono",
        ),
        migrations.AddField(
            model_name="registereduser",
            name="nacimiento",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="registereduser",
            name="pais_origen_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="kiddo_app.pais",
                verbose_name="País de origen",
            ),
        ),
    ]
