# Generated by Django 5.1 on 2024-08-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0009_project_level_raw_project_type_raw"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is active"),
        ),
        migrations.AddField(
            model_name="project",
            name="repositories_urls",
            field=models.JSONField(default=list, verbose_name="Repositories URLs"),
        ),
    ]
