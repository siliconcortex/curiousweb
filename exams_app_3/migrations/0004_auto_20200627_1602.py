# Generated by Django 3.0.3 on 2020-06-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app_3', '0003_auto_20200613_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exams_app_3/choice'),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exams_app_3/item'),
        ),
    ]
