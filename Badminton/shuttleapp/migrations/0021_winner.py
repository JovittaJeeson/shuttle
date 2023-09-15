# Generated by Django 4.2.4 on 2023-09-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0020_booking_delete_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='winners/')),
                ('name', models.CharField(max_length=100)),
                ('prize', models.CharField(max_length=100)),
            ],
        ),
    ]