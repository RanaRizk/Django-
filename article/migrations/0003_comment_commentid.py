# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150209_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentId',
            field=models.IntegerField(default=0),
        ),
    ]
