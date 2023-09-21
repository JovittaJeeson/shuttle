# Generated by Django 4.2.4 on 2023-09-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0022_eventuser_close_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='current_registrations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='max_registrations',
            field=models.PositiveIntegerField(default=100),
        ),
    ]