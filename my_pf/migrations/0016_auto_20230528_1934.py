# Generated by Django 3.2.18 on 2023-05-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0015_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='flag_nationality',
            field=models.ImageField(blank=True, null=True, upload_to='..media/flags/'),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='flag_residency',
            field=models.ImageField(blank=True, null=True, upload_to='..media/flags/'),
        ),
    ]
