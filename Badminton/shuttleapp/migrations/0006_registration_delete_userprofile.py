# Generated by Django 4.2.4 on 2023-09-06 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_type', models.CharField(max_length=10)),
                ('name1', models.CharField(max_length=100)),
                ('dob1', models.DateField()),
                ('name2', models.CharField(blank=True, max_length=100, null=True)),
                ('dob2', models.DateField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('declaration_accepted', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttleapp.eventuser')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]