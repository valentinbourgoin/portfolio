# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='slug')),
                ('class_name', models.CharField(max_length=255, null=True, verbose_name='class name', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug', unique_for_date=b'publication_date')),
                ('pict', models.ImageField(null=True, upload_to=b'img/entries/', blank=True)),
                ('publication_date', models.DateTimeField(default=datetime.datetime(2014, 9, 17, 23, 19, 10, 787418), verbose_name='publication date', db_index=True)),
                ('status', models.IntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'Offline'), (1, 'Online')])),
                ('body', models.TextField(verbose_name='body')),
                ('overview', models.TextField()),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='category', to='blog.Category')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            bases=(models.Model,),
        ),
    ]
