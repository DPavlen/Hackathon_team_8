# Generated by Django 4.2.6 on 2023-10-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidates", "0005_rename_level_education_education_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="location",
            field=models.CharField(
                max_length=150, verbose_name="Местонахождение"
            ),
        ),
    ]