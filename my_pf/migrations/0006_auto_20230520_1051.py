# Generated by Django 3.2.18 on 2023-05-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0005_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Database',
        ),
        migrations.DeleteModel(
            name='Framework',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.DeleteModel(
            name='VersionControl',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='databases',
            new_name='database_href1',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='frameworks',
            new_name='database_href2',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='languages',
            new_name='database_href3',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='version_control',
            new_name='database_href4',
        ),
        migrations.AddField(
            model_name='skills',
            name='database_href5',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='database_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_href1',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_href2',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_href3',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_href4',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_href5',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='framework_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_href1',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_href2',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_href3',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_href4',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_href5',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='language_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_href1',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_href2',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_href3',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_href4',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_href5',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='library_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_href1',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_href2',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_href3',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_href4',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_href5',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='version_control_name',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
