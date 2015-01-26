# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_remove_bookmark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
