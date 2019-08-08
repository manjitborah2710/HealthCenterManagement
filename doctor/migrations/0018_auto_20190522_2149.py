# Generated by Django 2.1.3 on 2019-05-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_auto_20190522_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicineissue',
            old_name='medicine_quantity',
            new_name='medicine_quantity_issued',
        ),
        migrations.AddField(
            model_name='medicineissue',
            name='dosage',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='medicineissue',
            name='medicine_quantity_prescribed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
