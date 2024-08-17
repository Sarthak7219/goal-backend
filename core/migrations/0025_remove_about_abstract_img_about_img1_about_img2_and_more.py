# Generated by Django 5.0.6 on 2024-08-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_about_abstract_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='abstract_img',
        ),
        migrations.AddField(
            model_name='about',
            name='img1',
            field=models.ImageField(null=True, upload_to='images/about/'),
        ),
        migrations.AddField(
            model_name='about',
            name='img2',
            field=models.ImageField(null=True, upload_to='images/about/'),
        ),
        migrations.AddField(
            model_name='about',
            name='img3',
            field=models.ImageField(null=True, upload_to='images/about/'),
        ),
        migrations.AddField(
            model_name='about',
            name='img4',
            field=models.ImageField(null=True, upload_to='images/about/'),
        ),
    ]
