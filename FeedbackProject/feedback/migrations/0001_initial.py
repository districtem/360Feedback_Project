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

        # Adding model 'FeedbackRecipient'
        db.create_table(u'feedback_feedbackrecipient', (
            (u'baseemployee_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feedback.BaseEmployee'], unique=True, primary_key=True)),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(default='This Fool does not yeat have a feedback coach', related_name='RecipientCoach', to=orm['feedback.BaseEmployee'])),
        ))
        db.send_create_signal(u'feedback', ['FeedbackRecipient'])

        # Adding model 'FeedbackGiver'
        db.create_table(u'feedback_feedbackgiver', (
            (u'baseemployee_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feedback.BaseEmployee'], unique=True, primary_key=True)),
            ('can_quote_giver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_use_giver_name', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('summarize_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('coach_chat_before_delivery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_judgement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackGiver'])

        # Adding model 'Feedback'
        db.create_table(u'feedback_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_given', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('feedback', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.FeedbackRecipient'])),
            ('giver', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.FeedbackGiver'])),
            ('fool_numerical_recommendation', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('top_of_game_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('next_level', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'BaseEmployee'
        db.delete_table(u'feedback_baseemployee')

        # Deleting model 'FeedbackRecipient'
        db.delete_table(u'feedback_feedbackrecipient')

        # Deleting model 'FeedbackGiver'
        db.delete_table(u'feedback_feedbackgiver')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')


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
            'fool_numerical_recommendation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackGiver']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_level': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.FeedbackRecipient']"}),
            'top_of_game_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'feedback.feedbackgiver': {
            'Meta': {'object_name': 'FeedbackGiver', '_ormbases': [u'feedback.BaseEmployee']},
            u'baseemployee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feedback.BaseEmployee']", 'unique': 'True', 'primary_key': 'True'}),
            'best_judgement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_quote_giver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_use_giver_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coach_chat_before_delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summarize_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient', '_ormbases': [u'feedback.BaseEmployee']},
            u'baseemployee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feedback.BaseEmployee']", 'unique': 'True', 'primary_key': 'True'}),
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'related_name': "'RecipientCoach'", 'to': u"orm['feedback.BaseEmployee']"})
        }
    }

    complete_apps = ['feedback']