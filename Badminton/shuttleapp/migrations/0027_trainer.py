# Generated by Django 4.2.4 on 2024-01-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0026_alter_eventuser_current_registrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
