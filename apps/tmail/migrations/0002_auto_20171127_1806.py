# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmail', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Template',
            new_name='EmailTemplate',
        ),
    ]
