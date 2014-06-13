# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseEmployee'
        db.create_table(u'feedback_baseemployee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_coach', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'feedback', ['BaseEmployee'])


    def backwards(self, orm):
        # Deleting model 'BaseEmployee'
        db.delete_table(u'feedback_baseemployee')


    models = {
        u'feedback.baseemployee': {
            'Meta': {'object_name': 'BaseEmployee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_coach': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['feedback']