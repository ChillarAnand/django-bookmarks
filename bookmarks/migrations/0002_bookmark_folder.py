# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='folder',
            field=models.ForeignKey(default='', to='bookmarks.Folder'),
            preserve_default=False,
        ),
    ]
