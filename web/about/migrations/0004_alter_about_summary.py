# Generated by Django 4.2.9 on 2024-01-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_summury_about_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.CharField(max_length=255, verbose_name='Short Summury'),
        ),
    ]
