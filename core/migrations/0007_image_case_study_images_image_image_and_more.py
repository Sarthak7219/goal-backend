# Generated by Django 5.0.6 on 2024-06-26 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='case_study_images',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.case_study'),
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=True, upload_to='images/all/'),
        ),
        migrations.AddField(
            model_name='image',
            name='workshop_images',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.workshop'),
        ),
    ]
