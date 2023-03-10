# Generated by Django 4.1.4 on 2023-01-05 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RDV', '0004_doctor_doctorspeciality_alter_rdv_doctorid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='DoctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RDV.doctor'),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='PatientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RDV.patient'),
        ),
    ]
