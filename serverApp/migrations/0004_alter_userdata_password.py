# Generated by Django 5.0.1 on 2024-10-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverApp', '0003_alter_userdata_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]