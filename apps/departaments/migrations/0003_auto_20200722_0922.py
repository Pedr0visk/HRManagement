# Generated by Django 3.0.7 on 2020-07-22 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('departaments', '0002_departament_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departament',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departaments', to='companies.Company'),
        ),
    ]
