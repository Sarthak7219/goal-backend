# Generated by Django 5.0.6 on 2024-05-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=20)),
                ('date_of_publishing', models.DateField()),
                ('publisher', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
