# Generated by Django 2.1.3 on 2019-05-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_auto_20190522_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineissue',
            name='medicine_quantity_issued',
            field=models.IntegerField(blank=True),
        ),
    ]
