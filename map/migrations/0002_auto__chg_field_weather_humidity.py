# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Weather.humidity'
        db.alter_column(u'map_weather', 'humidity', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Weather.humidity'
        raise RuntimeError("Cannot reverse this migration. 'Weather.humidity' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Weather.humidity'
        db.alter_column(u'map_weather', 'humidity', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'map.weather': {
            'Meta': {'object_name': 'Weather'},
            'humidity': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']