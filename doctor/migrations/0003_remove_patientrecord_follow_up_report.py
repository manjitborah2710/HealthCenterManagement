# Generated by Django 2.1.3 on 2018-12-03 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20181203_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientrecord',
            name='follow_up_report',
        ),
    ]