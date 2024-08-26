# Generated by Django 5.1 on 2024-08-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owasp", "0011_remove_project_repositories_urls_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="owasp_leaders",
        ),
        migrations.RemoveField(
            model_name="project",
            name="owasp_repositories_urls",
        ),
        migrations.AddField(
            model_name="project",
            name="leaders_raw",
            field=models.JSONField(default=list, verbose_name="Project leaders list"),
        ),
        migrations.AddField(
            model_name="project",
            name="repositories_raw",
            field=models.JSONField(default=list, verbose_name="Project repositories list"),
        ),
    ]
