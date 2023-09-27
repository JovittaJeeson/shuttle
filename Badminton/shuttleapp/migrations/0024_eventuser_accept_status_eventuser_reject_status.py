# Generated by Django 4.2.4 on 2023-09-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0023_eventuser_current_registrations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='accept_status',
            field=models.BooleanField(default=False, help_text='Accept Status'),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='reject_status',
            field=models.BooleanField(default=False, help_text='Reject Status'),
        ),
    ]