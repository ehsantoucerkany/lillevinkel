# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='color',
            field=models.CharField(default='N/A', max_length=30),
            preserve_default=False,
        ),
    ]
