# Generated by Django 5.0.6 on 2024-09-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_teammember_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(default='images/team_member/default.jpg', upload_to='images/team_member/'),
        ),
    ]
