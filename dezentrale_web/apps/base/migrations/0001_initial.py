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
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', auto_created=True, parent_link=True)),
                ('welcomeMessage', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
