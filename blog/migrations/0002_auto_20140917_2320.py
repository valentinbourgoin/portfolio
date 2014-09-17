# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='class_name',
        ),
        migrations.AlterField(
            model_name='entry',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 17, 23, 20, 12, 613217), verbose_name='publication date', db_index=True),
        ),
    ]
