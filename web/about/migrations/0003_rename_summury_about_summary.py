# Generated by Django 4.2.9 on 2024-01-30 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_summury'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='summury',
            new_name='summary',
        ),
    ]
