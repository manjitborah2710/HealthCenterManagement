# Generated by Django 2.1.3 on 2018-12-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20181203_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualrecord',
            name='date_of_leaving',
            field=models.DateField(blank=True),
        ),
    ]
