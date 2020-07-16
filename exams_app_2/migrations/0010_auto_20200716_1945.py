# Generated by Django 3.0.3 on 2020-07-16 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams_app_2', '0009_auto_20200716_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=5000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='discussion/comments')),
                ('thumbnail', models.ImageField(blank=True, upload_to='discussion/thumbnails')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(blank=True, max_length=5000)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='discussion/submissions')),
                ('thumbnail', models.ImageField(blank=True, upload_to='discussion/thumbnails')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(to='exams_app_2.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='submissions',
            field=models.ManyToManyField(to='exams_app_2.Submission'),
        ),
    ]