# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def 初始狀況表(app, editor):
    狀況陣列 = [
        "愛討論",
        "音檔：時間切毋著",
        "音檔：講話時有雜音",
        "音檔：無講話時有雜音",
        "音檔：兩人同齊講話",
        "音檔：有音樂",
        "詞：有外語詞",
        "詞：有合音",
        "詞：有唸毋著",
        "句：聽無佇咧講啥",
        "句：無合語感",
    ]
    語料狀況表 = app.get_model("語料庫", "語料狀況表")
    for 一狀況 in 狀況陣列:
        語料狀況表.objects.get_or_create(狀況=一狀況)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='語料狀況表',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('狀況', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': '狀況表',
                'verbose_name_plural': '狀況表',
            },
        ),
        migrations.CreateModel(
            name='語料表',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('聲音開始時間', models.FloatField()),
                ('聲音結束時間', models.FloatField()),
                ('語者', models.CharField(db_index=True, max_length=50)),
                ('漢字', models.TextField(blank=True)),
                ('本調臺羅', models.TextField(blank=True)),
                ('口語調臺羅', models.TextField(blank=True)),
                ('華語', models.TextField(blank=True)),
                ('校對時間', models.DateTimeField(auto_now=True)),
                ('頭一版資料', models.TextField(blank=True)),
                ('頭一版通用', models.TextField(blank=True)),
                ('sing5hong5舊編號', models.CharField(max_length=200, null=True)),
                ('sing5hong5新編號', models.CharField(max_length=200, null=True)),
                ('sing5hong5有揀出來用無', models.BooleanField(default=False)),
                ('校對者', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
                ('語料狀況', models.ManyToManyField(blank=True, to='語料庫.語料狀況表')),
            ],
            options={
                'verbose_name': '語料表',
                'verbose_name_plural': '語料表',
            },
        ),
        migrations.CreateModel(
            name='音檔表',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('類別', models.CharField(choices=[
                 ('戲劇', '戲劇'), ('朗讀', '朗讀'), ('新聞', '新聞'), ('對話', '對話')],
                    db_index=True, max_length=20)),
                ('原始檔', models.FileField(blank=True, upload_to='')),
                ('資料夾名', models.CharField(max_length=50)),
                ('聲音檔名', models.CharField(max_length=200)),
                ('聽拍檔名', models.CharField(max_length=200)),
                ('加入時間', models.DateTimeField(
                    auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['資料夾名', '聲音檔名', '聽拍檔名'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='音檔表',
            unique_together=set([('資料夾名', '聽拍檔名')]),
        ),
        migrations.AddField(
            model_name='語料表',
            name='音檔',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='資料', to='語料庫.音檔表'),
        ),
        migrations.RunPython(初始狀況表, lambda *x:x),
    ]
