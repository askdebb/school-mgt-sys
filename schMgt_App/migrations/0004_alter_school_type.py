# Generated by Django 4.2.4 on 2023-08-13 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schMgt_App', '0003_alter_school_sch_no_alter_school_tel_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('PU', 'Public'), ('PV', 'Private')], default='PU', max_length=7),
        ),
    ]
