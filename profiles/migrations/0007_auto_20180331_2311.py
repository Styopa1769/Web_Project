# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 23:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_blog_is_archive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('name', 'id'), 'verbose_name': '\u0411\u043b\u043e\u0433', 'verbose_name_plural': '\u0411\u043b\u043e\u0433\u0438'},
        ),
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='\u0411\u043b\u043e\u0433 \u0432 \u0430\u0440\u0445\u0438\u0432\u0435'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f \u0431\u043b\u043e\u0433\u0430'),
        ),
    ]
