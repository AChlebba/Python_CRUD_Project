# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-24 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dziennik_posilkow', '0005_auto_20170524_2256'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Zawodnik',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='person',
            new_name='zawodnik',
        ),
    ]
