# Generated by Django 3.2.18 on 2023-05-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0012_auto_20230528_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headings',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]