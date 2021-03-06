# Generated by Django 2.2.16 on 2021-05-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_message', '0002_auto_20210528_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config_message',
            name='camera_model',
            field=models.PositiveIntegerField(choices=[(6, 'BSD（06）'), (2, '前视模式（02）'), (1, '相机模式（01）'), (3, '相机+前视（03）'), (4, '环视（04）'), (5, '后视（05）')], default=1, verbose_name='相机模式'),
        ),
        migrations.AlterField(
            model_name='config_message',
            name='create_time',
            field=models.DateTimeField(verbose_name='出厂日期'),
        ),
    ]
