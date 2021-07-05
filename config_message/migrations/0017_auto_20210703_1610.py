# Generated by Django 2.2.16 on 2021-07-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_message', '0016_auto_20210702_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config_message',
            name='camera_model',
            field=models.IntegerField(choices=[(3, '相机+前视（03）'), (4, '环视（04）'), (6, 'BSD（06）'), (1, '相机模式（01）'), (2, '前视模式（02）'), (5, '后视（05）')], default=1, verbose_name='相机模式'),
        ),
    ]
