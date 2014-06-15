# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedbackGiver'
        db.create_table(u'feedback_feedbackgiver', (
            (u'employee_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feedback.Employee'], unique=True, primary_key=True)),
            ('feedback', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Feedback'], blank=True)),
            ('can_quote_giver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_use_giver_name', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('summarize_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('coach_chat_before_delivery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_judgement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackGiver'])


    def backwards(self, orm):
        # Deleting model 'FeedbackGiver'
        db.delete_table(u'feedback_feedbackgiver')


    models = {
        u'feedback.employee': {
            'Meta': {'object_name': 'Employee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_coach': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'date_given': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fool_numerical_recommendation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_level': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackRecipient']"}),
            'top_of_game_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'feedback.feedbackgiver': {
            'Meta': {'object_name': 'FeedbackGiver', '_ormbases': [u'feedback.Employee']},
            'best_judgement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_quote_giver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_use_giver_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coach_chat_before_delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'employee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feedback.Employee']", 'unique': 'True', 'primary_key': 'True'}),
            'feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Feedback']", 'blank': 'True'}),
            'summarize_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient', '_ormbases': [u'feedback.Employee']},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'related_name': "'RecipientCoach'", 'to': u"orm['feedback.Employee']"}),
            u'employee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feedback.Employee']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']