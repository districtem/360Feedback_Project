# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'feedback_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_coach', self.gf('django.db.models.fields.BooleanField')()),
            ('is_available_to_coach', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['Employee'])

        # Adding model 'FeedbackRecipient'
        db.create_table(u'feedback_feedbackrecipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.Employee'])),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(default='This Fool does not yeat have a feedback coach', related_name='RecipientCoach', to=orm['feedback.Employee'])),
        ))
        db.send_create_signal(u'feedback', ['FeedbackRecipient'])

        # Adding model 'Feedback'
        db.create_table(u'feedback_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_given', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.FeedbackRecipient'])),
            ('fool_numerical_recommendation', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('top_of_game_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('next_level', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['Feedback'])

        # Adding model 'FeedbackGiver'
        db.create_table(u'feedback_feedbackgiver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('giver', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['feedback.Employee'])),
            ('feedback', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Feedback'], blank=True)),
            ('can_quote_giver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_use_giver_name', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('summarize_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('coach_chat_before_delivery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_judgement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackGiver'])

        # Adding model 'FeedbackInvitation'
        db.create_table(u'feedback_feedbackinvitation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invite_sener', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.FeedbackRecipient'])),
            ('invite_receiver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.FeedbackGiver'])),
            ('invite_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['FeedbackInvitation'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'feedback_employee')

        # Deleting model 'FeedbackRecipient'
        db.delete_table(u'feedback_feedbackrecipient')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')

        # Deleting model 'FeedbackGiver'
        db.delete_table(u'feedback_feedbackgiver')

        # Deleting model 'FeedbackInvitation'
        db.delete_table(u'feedback_feedbackinvitation')


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
            'feedback': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Feedback']", 'blank': 'True'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summarize_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'feedback.feedbackinvitation': {
            'Meta': {'object_name': 'FeedbackInvitation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invite_receiver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.FeedbackGiver']"}),
            'invite_sener': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.FeedbackRecipient']"})
        },
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'related_name': "'RecipientCoach'", 'to': u"orm['feedback.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['feedback.Employee']"})
        }
    }

    complete_apps = ['feedback']