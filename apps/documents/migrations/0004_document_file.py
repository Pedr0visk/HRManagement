# Generated by Django 3.0.7 on 2020-07-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20200714_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]
