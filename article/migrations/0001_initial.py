# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('like', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=b'static/images/article')),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('onComment', models.BooleanField(default=False)),
                ('like', models.IntegerField(default=0)),
                ('body', models.TextField()),
                ('articleId', models.ForeignKey(to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='TagOnArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=200)),
                ('articleId', models.ForeignKey(to='article.Article')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'static/images/user')),
                ('logWithFb', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(to='article.User'),
        ),
    ]
