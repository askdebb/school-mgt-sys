# Generated by Django 4.2.4 on 2023-09-09 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schMgt_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherrecord',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacherrecord',
            name='othernames',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='teacherrecord',
            name='surname',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teacherrecord',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]