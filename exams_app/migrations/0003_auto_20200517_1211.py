# Generated by Django 3.0.3 on 2020-05-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams_app', '0002_auto_20200516_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorya',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='categorya',
            name='exams',
            field=models.ManyToManyField(blank=True, null=True, to='exams_app.Exam'),
        ),
        migrations.AlterField(
            model_name='categoryb',
            name='categoryas',
            field=models.ManyToManyField(blank=True, null=True, to='exams_app.CategoryA'),
        ),
        migrations.AlterField(
            model_name='categoryb',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mcq',
            name='question',
            field=models.TextField(default='', max_length=1000),
        ),
    ]