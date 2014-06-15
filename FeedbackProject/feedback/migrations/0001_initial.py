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
        ))
        db.send_create_signal(u'feedback', ['Employee'])

        # Adding model 'FeedbackRecipient'
        db.create_table(u'feedback_feedbackrecipient', (
            (u'employee_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['feedback.Employee'], unique=True, primary_key=True)),
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


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'feedback_employee')

        # Deleting model 'FeedbackRecipient'
        db.delete_table(u'feedback_feedbackrecipient')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')


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
        u'feedback.feedbackrecipient': {
            'Meta': {'object_name': 'FeedbackRecipient', '_ormbases': [u'feedback.Employee']},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'default': "'This Fool does not yeat have a feedback coach'", 'related_name': "'RecipientCoach'", 'to': u"orm['feedback.Employee']"}),
            u'employee_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['feedback.Employee']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']