# Generated by Django 3.2.16 on 2022-11-07 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_membermaster_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transum',
            options={'verbose_name': 'MOS_TransSum', 'verbose_name_plural': 'MOS_TransSum'},
        ),
    ]