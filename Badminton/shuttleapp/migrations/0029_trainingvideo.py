# Generated by Django 4.2.2 on 2024-02-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttleapp', '0028_trainingregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('trainer', models.CharField(max_length=100)),
                ('video_file', models.FileField(upload_to='training_videos/')),
            ],
        ),
    ]