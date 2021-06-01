# Generated by Django 2.2.16 on 2021-05-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_message', '0010_auto_20210531_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config_message',
            name='camera_model',
            field=models.PositiveIntegerField(choices=[(4, '环视（04）'), (3, '相机+前视（03）'), (1, '相机模式（01）'), (5, '后视（05）'), (6, 'BSD（06）'), (2, '前视模式（02）')], default=1, verbose_name='相机模式'),
        ),
    ]
