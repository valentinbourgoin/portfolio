# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20140917_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 18, 21, 12, 44, 666743), verbose_name='publication date', db_index=True),
        ),
    ]
