# Generated by Django 5.0.6 on 2024-07-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_resources_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='link',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]