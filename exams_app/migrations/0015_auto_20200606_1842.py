# Generated by Django 3.0.3 on 2020-06-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app', '0014_auto_20200523_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='explanation',
        ),
        migrations.AddField(
            model_name='mcq',
            name='explanation',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]