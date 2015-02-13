# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment_commentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeByUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userLike', models.IntegerField(default=0)),
                ('articleId', models.ForeignKey(to='article.Article')),
                ('userId', models.ForeignKey(to='article.User_1')),
            ],
        ),
    ]
