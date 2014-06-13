# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feedback.recipient'
        db.delete_column(u'feedback_feedback', 'recipient_id')


    def backwards(self, orm):
        # Adding field 'Feedback.recipient'
        db.add_column(u'feedback_feedback', 'recipient',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.BaseEmployee'], null=True),
                      keep_default=False)


    models = {
        u'feedback.baseemployee': {
            'Meta': {'object_name': 'BaseEmployee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_coach': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'date_given': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']