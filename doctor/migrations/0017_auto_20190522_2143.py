# Generated by Django 2.1.3 on 2019-05-22 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_auto_20190522_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='patient_id',
            field=models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='doctor.StudentRecord'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_id',
            field=models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='doctor.StudentRecord'),
        ),
    ]
