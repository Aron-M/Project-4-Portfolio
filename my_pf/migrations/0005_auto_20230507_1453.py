# Generated by Django 3.2.18 on 2023-05-07 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0004_auto_20230507_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='language',
            name='image2',
            field=models.ImageField(default='staticfiles/media/languages_images/html5.png', upload_to='skills/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='image3',
            field=models.ImageField(default='staticfiles/media/languages_images/css3.png', upload_to='skills/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='image4',
            field=models.ImageField(default='staticfiles/media/languages_images/JS.png', upload_to='skills/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='image5',
            field=models.ImageField(default='staticfiles/media/languages_images/css3.png', upload_to='skills/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
            preserve_default=False,
        ),
    ]
