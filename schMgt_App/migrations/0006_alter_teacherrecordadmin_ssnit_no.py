# Generated by Django 4.2.4 on 2023-09-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schMgt_App', '0005_teacherrecord_form_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherrecordadmin',
            name='SSNIT_no',
            field=models.CharField(max_length=13),
        ),
    ]
