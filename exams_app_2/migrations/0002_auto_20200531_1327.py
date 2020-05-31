# Generated by Django 3.0.3 on 2020-05-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='exam',
            name='file',
        ),
        migrations.AddField(
            model_name='exam',
            name='files',
            field=models.ManyToManyField(to='exams_app_2.ExamFile'),
        ),
    ]
