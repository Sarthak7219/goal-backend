# Generated by Django 5.0.6 on 2024-07-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_stories_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='contact',
        ),
        migrations.AddField(
            model_name='teammember',
            name='apn_profile_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
