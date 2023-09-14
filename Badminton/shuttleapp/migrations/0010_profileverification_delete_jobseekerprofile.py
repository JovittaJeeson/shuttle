# Generated by Django 4.2.4 on 2023-09-12 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuttleapp', '0009_jobseekerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('proof_type', models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('Voters Card', 'Voters Card'), ('Passport', 'Passport')], max_length=255)),
                ('buisness_license', models.FileField(upload_to='uploads/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='JobseekerProfile',
        ),
    ]