# Generated by Django 4.2.4 on 2023-08-31 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membershipapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MembershipPlan',
            new_name='SubscriptionPlan',
        ),
    ]
