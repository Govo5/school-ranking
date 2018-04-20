# Generated by Django 2.0.4 on 2018-04-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollHighSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jibun', models.CharField(max_length=50)),
                ('road', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('school_code', models.CharField(max_length=50)),
                ('region_code', models.CharField(max_length=50)),
                ('graduate', models.FloatField()),
                ('general', models.FloatField()),
                ('characterization', models.FloatField()),
                ('science', models.FloatField()),
                ('foreigner', models.FloatField()),
                ('art', models.FloatField()),
                ('meister', models.FloatField()),
                ('private', models.FloatField()),
                ('public', models.FloatField()),
                ('etc', models.FloatField()),
                ('job', models.FloatField()),
                ('nothing', models.FloatField()),
                ('data_type', models.CharField(max_length=5)),
            ],
        ),
    ]
