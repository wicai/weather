# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweets'
        db.create_table(u'map_tweets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Region'])),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'map', ['Tweets'])

        # Adding model 'Region'
        db.create_table(u'map_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'map', ['Region'])

        # Deleting field 'Weather.latitude'
        db.delete_column(u'map_weather', 'latitude')

        # Deleting field 'Weather.longitude'
        db.delete_column(u'map_weather', 'longitude')

        # Adding field 'Weather.region'
        db.add_column(u'map_weather', 'region',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['map.Region']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Tweets'
        db.delete_table(u'map_tweets')

        # Deleting model 'Region'
        db.delete_table(u'map_region')

        # Adding field 'Weather.latitude'
        db.add_column(u'map_weather', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Weather.longitude'
        db.add_column(u'map_weather', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Weather.region'
        db.delete_column(u'map_weather', 'region_id')


    models = {
        u'map.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'map.tweets': {
            'Meta': {'object_name': 'Tweets'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Region']"}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'map.weather': {
            'Meta': {'object_name': 'Weather'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Region']"}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']