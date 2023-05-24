# Generated by Django 3.2.18 on 2023-05-24 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.URLField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('progress', models.ImageField(blank=True, null=True, upload_to='progress/')),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_pf.skill')),
            ],
        ),
    ]
