# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0039_auto_20200331_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_post',
            field=models.BooleanField(default=False, verbose_name='Featured Post'),
        ),
    ]
