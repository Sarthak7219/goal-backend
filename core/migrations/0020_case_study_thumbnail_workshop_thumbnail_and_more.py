# Generated by Django 5.0.6 on 2025-03-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_resources_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_study',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/case_study/thumbnails/'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/workshop/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='mode',
            field=models.CharField(choices=[('offline', 'Offline'), ('online', 'Online'), ('hybrid', 'Hybrid')], default='offline', max_length=30),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='venue',
            field=models.CharField(max_length=500),
        ),
    ]
