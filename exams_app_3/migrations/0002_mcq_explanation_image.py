# Generated by Django 3.0.3 on 2020-06-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app_3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='explanation_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
