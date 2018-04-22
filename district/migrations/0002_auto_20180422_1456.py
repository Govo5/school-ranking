# Generated by Django 2.0.4 on 2018-04-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='administration_category',
            field=models.IntegerField(help_text='행정구역분류'),
        ),
        migrations.AlterField(
            model_name='district',
            name='administration_code',
            field=models.IntegerField(help_text='행정기관코드'),
        ),
        migrations.AlterField(
            model_name='district',
            name='legal_code',
            field=models.IntegerField(help_text='법정동코드'),
        ),
    ]
