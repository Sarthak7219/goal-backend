# Generated by Django 5.0.6 on 2024-06-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_teammember_alter_resources_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
