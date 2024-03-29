# Generated by Django 2.0.4 on 2018-04-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0005_auto_20180422_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='administration_category',
            field=models.BigIntegerField(help_text='행정구역분류'),
        ),
        migrations.AlterField(
            model_name='code',
            name='administration_code',
            field=models.BigIntegerField(help_text='행정기관코드'),
        ),
        migrations.AlterField(
            model_name='code',
            name='legal_code',
            field=models.BigIntegerField(help_text='법정동코드'),
        ),
    ]
