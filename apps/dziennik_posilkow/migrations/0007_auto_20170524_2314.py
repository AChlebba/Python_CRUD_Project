# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-24 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dziennik_posilkow', '0006_auto_20170524_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zawodnik',
            old_name='name',
            new_name='imie',
        ),
    ]
