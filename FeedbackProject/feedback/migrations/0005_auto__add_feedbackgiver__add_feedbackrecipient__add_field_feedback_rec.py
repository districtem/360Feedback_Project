# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedbackGiver'
        db.create_table(u'feedback_feedbackgiver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feedback_to_give', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Feedback'], null=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackGiver'])

        # Adding model 'FeedbackRecipient'
        db.create_table(u'feedback_feedbackrecipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(default='This Fool does not yeat have a feedback coach', to=orm['feedback.BaseEmployee'])),
        ))
        db.send_create_signal(u'feedback', ['FeedbackRecipient'])

        # Adding field 'Feedback.recipient'
        db.add_column(u'feedback_feedback', 'recipient',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.FeedbackRecipient']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FeedbackGiver'
        db.delete_table(u'feedback_feedbackgiver')

        # Deleting model 'FeedbackRecipient'
        db.delete_table(u'feedback_feedbackrecipient')

        # Deleting field 'Feedback.recipient'
        db.delete_column(u'feedback_feedback', 'recipient_id')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackRecipient']"})
        },
        u'feedback.feedbackgiver': {
            'Meta': {'object_name': 'FeedbackGiver'},
            'feedback_to_give': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Feedback']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'to': u"orm['feedback.BaseEmployee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']