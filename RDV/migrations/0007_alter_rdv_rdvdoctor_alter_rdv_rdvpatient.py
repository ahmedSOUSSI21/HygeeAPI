# Generated by Django 4.1.4 on 2023-01-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RDV', '0006_rename_doctorid_rdv_rdvdoctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='RdvDoctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctorId', to='RDV.doctor'),
        ),
        migrations.AlterField(
            model_name='rdv',
            name='RdvPatient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientId', to='RDV.patient'),
        ),
    ]
