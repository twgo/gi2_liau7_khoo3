# Generated by Django 2.1.dev20171208073737 on 2017-12-08 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('檢查工具', '0004_對齊狀態表_本調口語調對應'),
    ]

    operations = [
        migrations.RenameField(
            model_name='對齊狀態表',
            old_name='狀態',
            new_name='漢字本調對應',
        ),
    ]
