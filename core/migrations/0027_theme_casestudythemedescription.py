# Generated by Django 5.0.6 on 2024-08-16 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_teammember_website_link_alter_resources_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseStudyThemeDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('case_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_study_themes', to='core.case_study')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_study_themes', to='core.theme')),
            ],
        ),
    ]
