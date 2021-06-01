# Generated by Django 2.2.16 on 2021-05-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_message', '0008_auto_20210528_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config_message',
            name='camera_model',
            field=models.PositiveIntegerField(choices=[(3, '相机+前视（03）'), (5, '后视（05）'), (2, '前视模式（02）'), (6, 'BSD（06）'), (4, '环视（04）'), (1, '相机模式（01）')], default=1, verbose_name='相机模式'),
        ),
    ]
