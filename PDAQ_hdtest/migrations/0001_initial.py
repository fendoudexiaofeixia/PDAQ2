# Generated by Django 2.2.16 on 2021-05-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDAQ_hd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_address', models.CharField(max_length=20, unique=True, verbose_name='IP地址')),
                ('hd_version', models.CharField(blank=True, max_length=10, null=True, verbose_name='硬件版本')),
                ('系统自启', models.CharField(blank=True, max_length=20, null=True, verbose_name='系统自启')),
                ('时间同步', models.CharField(blank=True, max_length=20, null=True, verbose_name='时间同步')),
                ('相机接口', models.CharField(blank=True, max_length=20, null=True, verbose_name='相机接口')),
                ('GPS', models.CharField(blank=True, max_length=20, null=True, verbose_name='GPS')),
                ('SATA写入速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='SATA写入速率')),
                ('SATA读取速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='SATA读取速率')),
                ('USB1读取速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='USB1读取速率')),
                ('USB1写入速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='USB1写入速率')),
                ('USB2写入速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='USB2写入速率')),
                ('USB2读取速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='USB2读取速率')),
                ('SD卡读取速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='SD卡读取速率')),
                ('SD卡写入速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='SD卡写入速率')),
                ('网口速率', models.CharField(blank=True, max_length=30, null=True, verbose_name='网口速率')),
                ('移动网速', models.CharField(blank=True, max_length=30, null=True, verbose_name='4G速率')),
                ('ICCID', models.CharField(blank=True, max_length=30, null=True, verbose_name='ICCID')),
                ('MEID', models.CharField(blank=True, max_length=30, null=True, verbose_name='MEID')),
                ('IMEI', models.CharField(blank=True, max_length=30, null=True, verbose_name='IMEI')),
                ('CAN板状态', models.CharField(blank=True, max_length=30, null=True, verbose_name='CAN板状态')),
                ('系统版本', models.CharField(blank=True, max_length=50, null=True, verbose_name='系统版本')),
                ('内核版本', models.CharField(blank=True, max_length=50, null=True, verbose_name='内核版本')),
                ('PCB版本', models.CharField(blank=True, max_length=50, null=True, verbose_name='PCB版本')),
                ('添加时间', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('test_result', models.CharField(max_length=5, verbose_name='测试结果')),
                ('Operators', models.CharField(blank=True, max_length=20, null=True, verbose_name='运行商')),
                ('Activation_time', models.CharField(blank=True, max_length=50, null=True, verbose_name='激活时间')),
                ('Expiration_time', models.CharField(blank=True, max_length=50, null=True, verbose_name='过期时间')),
                ('Card_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='卡片状态')),
                ('Set_meal', models.CharField(blank=True, max_length=10, null=True, verbose_name='套餐')),
                ('Set_meal_used', models.CharField(blank=True, max_length=20, null=True, verbose_name='套餐已用')),
                ('test_file', models.FileField(blank=True, null=True, upload_to='test_file', verbose_name='测试文件')),
            ],
            options={
                'verbose_name': 'PDAQ硬件测试信息',
                'verbose_name_plural': 'PDAQ硬件测试信息',
            },
        ),
    ]