# Generated by Django 2.1.3 on 2019-03-14 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20190314_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineissue',
            name='medicine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Medicine'),
        ),
    ]
