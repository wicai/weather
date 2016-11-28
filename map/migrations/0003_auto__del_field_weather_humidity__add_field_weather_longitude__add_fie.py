# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Weather.humidity'
        db.delete_column(u'map_weather', 'humidity')

        # Adding field 'Weather.longitude'
        db.add_column(u'map_weather', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Weather.latitude'
        db.add_column(u'map_weather', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Weather.humidity'
        db.add_column(u'map_weather', 'humidity',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Deleting field 'Weather.longitude'
        db.delete_column(u'map_weather', 'longitude')

        # Deleting field 'Weather.latitude'
        db.delete_column(u'map_weather', 'latitude')


    models = {
        u'map.weather': {
            'Meta': {'object_name': 'Weather'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']