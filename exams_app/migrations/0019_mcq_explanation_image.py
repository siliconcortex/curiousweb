# Generated by Django 3.0.3 on 2020-06-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app', '0018_auto_20200609_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='explanation_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
