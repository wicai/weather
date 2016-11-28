# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stats'
        db.create_table(u'map_stats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Region'])),
            ('ratio', self.gf('django.db.models.fields.FloatField')()),
            ('trating', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'map', ['Stats'])


        # Changing field 'Tweets.tweet'
        db.alter_column(u'map_tweets', 'tweet', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting model 'Stats'
        db.delete_table(u'map_stats')


        # Changing field 'Tweets.tweet'
        db.alter_column(u'map_tweets', 'tweet', self.gf('django.db.models.fields.CharField')(max_length=150))

    models = {
        u'map.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {})
        },
        u'map.stats': {
            'Meta': {'object_name': 'Stats'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ratio': ('django.db.models.fields.FloatField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Region']"}),
            'trating': ('django.db.models.fields.FloatField', [], {})
        },
        u'map.tweets': {
            'Meta': {'object_name': 'Tweets'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Region']"}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'map.weather': {
            'Meta': {'object_name': 'Weather'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['map.Region']"}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['map']