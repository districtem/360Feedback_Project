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
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('coach', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='coach', null=True, to=orm['auth.User'])),
            ('is_coach', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['Employee'])

        # Adding model 'FeedbackRequest'
        db.create_table(u'feedback_feedbackrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requestor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='FeedbackRequestor', to=orm['feedback.Employee'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='RequestRecipient', to=orm['feedback.Employee'])),
        ))
        db.send_create_signal(u'feedback', ['FeedbackRequest'])

        # Adding model 'Feedback'
        db.create_table(u'feedback_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_given', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='FeedbackRecipient', to=orm['feedback.Employee'])),
            ('giver', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='FeedbackGiver', to=orm['feedback.Employee'])),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.FeedbackRequest'], null=True, blank=True)),
            ('fool_numerical_recommendation', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('top_of_game_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('next_level', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('can_quote_giver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_use_giver_name', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('summarize_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('coach_chat_before_delivery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_judgement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'feedback', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'feedback_employee')

        # Deleting model 'FeedbackRequest'
        db.delete_table(u'feedback_feedbackrequest')

        # Deleting model 'Feedback'
        db.delete_table(u'feedback_feedback')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feedback.employee': {
            'Meta': {'object_name': 'Employee'},
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'coach'", 'null': 'True', 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_coach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'feedback.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'best_judgement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_quote_giver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_use_giver_name': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'coach_chat_before_delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_given': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fool_numerical_recommendation': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'FeedbackGiver'", 'to': u"orm['feedback.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_level': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'FeedbackRecipient'", 'to': u"orm['feedback.Employee']"}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.FeedbackRequest']", 'null': 'True', 'blank': 'True'}),
            'summarize_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'top_of_game_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'feedback.feedbackrequest': {
            'Meta': {'object_name': 'FeedbackRequest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'RequestRecipient'", 'to': u"orm['feedback.Employee']"}),
            'requestor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'FeedbackRequestor'", 'to': u"orm['feedback.Employee']"})
        }
    }

    complete_apps = ['feedback']