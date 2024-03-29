# Generated by Django 3.0.3 on 2020-05-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app', '0013_auto_20200522_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examticket',
            old_name='date_taken',
            new_name='date_finish',
        ),
        migrations.AddField(
            model_name='examticket',
            name='answers',
            field=models.ManyToManyField(to='exams_app.Choice'),
        ),
        migrations.AddField(
            model_name='examticket',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]
