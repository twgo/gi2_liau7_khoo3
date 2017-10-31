# Generated by Django 2.1.dev20171017102832 on 2017-10-30 08:12

from django.db import migrations, models
import django.db.models.deletion
from 校對工具.檢查本調拼音 import 檢查本調拼音


def 初始對齊狀態(apps, editor):
    語料表 = apps.get_model('語料庫', '語料表')
    對齊狀態表 = apps.get_model('語料庫', '對齊狀態表')
    for 一語料 in 語料表.objects.all():
        print(一語料.漢字, 一語料.本調臺羅)
        錯誤結果 = 檢查本調拼音(一語料.漢字, 一語料.本調臺羅)
        一狀態 = 對齊狀態表(狀態=錯誤結果)
        一狀態.save()
        一語料.對齊狀態 = 一狀態
        一語料.save()


class Migration(migrations.Migration):

    dependencies = [
        ('語料庫', '0005_kaldi篩掉表_討論表'),
    ]

    operations = [
        migrations.CreateModel(
            name='對齊狀態表',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('狀態', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='語料表',
            name='對齊狀態',
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='語料庫.對齊狀態表'),
        ),
        migrations.RunPython(初始對齊狀態, lambda *x:x)
    ]
