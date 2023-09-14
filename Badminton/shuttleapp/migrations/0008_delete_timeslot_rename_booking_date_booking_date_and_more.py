# Generated by Django 4.2.4 on 2023-09-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0007_booking_timeslot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeSlot',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='client_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='client_phone',
            field=models.CharField(max_length=15),
        ),
    ]