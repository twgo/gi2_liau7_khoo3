# Generated by Django 2.1.dev20171207101724 on 2017-12-08 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('語料庫', '0009_auto_20171201_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='對齊狀態表',
            name='語料',
        ),
        migrations.DeleteModel(
            name='對齊狀態表',
        ),
    ]
