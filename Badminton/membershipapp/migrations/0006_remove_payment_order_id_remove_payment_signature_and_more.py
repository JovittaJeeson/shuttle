# Generated by Django 4.2.4 on 2023-10-04 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membershipapp', '0005_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='signature',
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
