# Generated by Django 3.0 on 2019-12-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20191227_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
    ]