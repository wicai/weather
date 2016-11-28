# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weather'
        db.create_table(u'map_weather', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('temperature', self.gf('django.db.models.fields.IntegerField')()),
            ('humidity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'map', ['Weather'])


    def backwards(self, orm):
        # Deleting model 'Weather'
        db.delete_table(u'map_weather')


    models = {
        u'map.weather': {
            'Meta': {'object_name': 'Weather'},
            'humidity': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']