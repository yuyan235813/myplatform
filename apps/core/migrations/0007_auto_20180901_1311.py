# Generated by Django 2.0 on 2018-09-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180901_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='icon',
            field=models.ImageField(upload_to='media', verbose_name='图片地址'),
        ),
    ]
