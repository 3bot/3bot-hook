# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threebot_hook', '0002_remove_hook_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='repo',
            field=models.CharField(help_text='Leave blank. Field is not used in the current version.', max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hook',
            name='secret',
            field=models.CharField(help_text='Leave blank. Field is not used in the current version.', max_length=255, blank=True, null=True),
        ),
    ]
