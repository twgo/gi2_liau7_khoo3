# Generated by Django 2.1.dev20171218093347 on 2017-12-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('語料庫', '0011_auto_20171211_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='語料表',
            name='頭一版轉出來的口語調臺羅',
            field=models.TextField(blank=True),
        ),
    ]
