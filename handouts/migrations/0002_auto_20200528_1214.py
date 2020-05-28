# Generated by Django 3.0.3 on 2020-05-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handouts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandoutFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='handout',
            name='file',
        ),
        migrations.AddField(
            model_name='handout',
            name='files',
            field=models.ManyToManyField(to='handouts.HandoutFile'),
        ),
    ]
