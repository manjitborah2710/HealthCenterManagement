# Generated by Django 2.1.3 on 2018-12-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_remove_patientrecord_follow_up_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='primary_ingredient',
            field=models.CharField(max_length=50),
        ),
    ]
