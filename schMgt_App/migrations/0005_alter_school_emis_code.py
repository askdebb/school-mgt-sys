# Generated by Django 4.2.4 on 2023-08-13 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schMgt_App', '0004_alter_school_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='emis_code',
            field=models.CharField(max_length=50),
        ),
    ]