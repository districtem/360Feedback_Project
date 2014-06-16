# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feedback.giver'
        db.add_column(u'feedback_feedback', 'giver',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.FeedbackGiver']),
                      keep_default=False)

        # Deleting field 'FeedbackGiver.feedback'
        db.delete_column(u'feedback_feedbackgiver', 'feedback_id')


    def backwards(self, orm):
        # Deleting field 'Feedback.giver'
        db.delete_column(u'feedback_feedback', 'giver_id')

        # Adding field 'FeedbackGiver.feedback'
        db.add_column(u'feedback_feedbackgiver', 'feedback',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.Feedback'], blank=True),
                      keep_default=False)


    models = {
        u'feedback.employee': {
            'Meta': {'object_name': 'Employee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_available_to_coach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_coach': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'date_given': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fool_numerical_recommendation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackGiver']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_level': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackRecipient']"}),
            'top_of_game_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'feedback.feedbackgiver': {
            'Meta': {'object_name': 'FeedbackGiver'},
            'best_judgement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_quote_giver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_use_giver_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coach_chat_before_delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summarize_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'feedback.feedbackinvitation': {
            'Meta': {'object_name': 'FeedbackInvitation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invite_receiver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Employee']"}),
            'invite_sender': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.FeedbackRecipient']"})
        },
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'related_name': "'RecipientCoach'", 'to': u"orm['feedback.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.Employee']"})
        }
    }

    complete_apps = ['feedback']