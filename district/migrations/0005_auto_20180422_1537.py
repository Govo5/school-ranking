# Generated by Django 2.0.4 on 2018-04-22 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0004_auto_20180422_1535'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='code',
            unique_together={('administration_code', 'administration_name', 'legal_code', 'legal_name')},
        ),
    ]
