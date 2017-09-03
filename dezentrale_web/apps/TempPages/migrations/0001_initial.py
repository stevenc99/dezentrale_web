# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, serialize=False, to='wagtailcore.Page', auto_created=True, primary_key=True)),
                ('devMessage', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
