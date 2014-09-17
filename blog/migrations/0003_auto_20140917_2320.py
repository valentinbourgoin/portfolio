# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140917_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='class_name',
            field=models.CharField(max_length=255, null=True, verbose_name='class name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 17, 23, 20, 30, 91038), verbose_name='publication date', db_index=True),
        ),
    ]
