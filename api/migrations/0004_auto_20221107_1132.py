# Generated by Django 3.2.16 on 2022-11-07 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20221105_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customermaster',
            options={'verbose_name': 'CustomerMaster'},
        ),
        migrations.AlterModelOptions(
            name='membermaster',
            options={'verbose_name': 'MemberMaster'},
        ),
        migrations.AlterModelOptions(
            name='mos_sales',
            options={'verbose_name': 'MOS_Sales', 'verbose_name_plural': 'MOS_Sale'},
        ),
    ]