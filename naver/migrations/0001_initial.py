# Generated by Django 2.0.4 on 2018-04-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('expired_at', models.DateTimeField(verbose_name='date expired')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
