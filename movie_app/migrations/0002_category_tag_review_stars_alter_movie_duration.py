# Generated by Django 4.2.1 on 2023-11-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=7),
        ),
    ]
