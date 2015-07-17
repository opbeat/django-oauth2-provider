# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0002_auto_20150424_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='redirect_uri',
            field=models.URLField(help_text=b"Your application's callback URL"),
        ),
        migrations.AlterField(
            model_name='client',
            name='url',
            field=models.CharField(help_text=b"Your application's URL.", max_length=200, blank=True),
        ),
        migrations.AlterModelTable(
            name='accesstoken',
            table='oauth_accesstoken',
        ),
        migrations.AlterModelTable(
            name='client',
            table='oauth_client',
        ),
        migrations.AlterModelTable(
            name='grant',
            table='oauth_grant',
        ),
        migrations.AlterModelTable(
            name='refreshtoken',
            table='oauth_refreshtoken',
        ),
    ]
