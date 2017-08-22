# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20170207_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(max_length=30)),
                ('social_link', models.CharField(max_length=100, blank=True)),
                ('user_profile', models.ForeignKey(related_name='social_links', to='student.UserProfile')),
            ],
        ),
    ]
