# Generated by Django 4.2.4 on 2024-03-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fixture", "0009_auto_20171124_1904"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fixture",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="match",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]