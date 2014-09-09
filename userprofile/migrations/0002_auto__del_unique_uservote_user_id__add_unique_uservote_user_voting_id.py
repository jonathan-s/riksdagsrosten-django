# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'UserVote', fields ['user', 'id']
        db.delete_unique('userprofile_uservote', ['user_id', 'id'])

        # Adding unique constraint on 'UserVote', fields ['user', 'voting_id']
        db.create_unique('userprofile_uservote', ['user_id', 'voting_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserVote', fields ['user', 'voting_id']
        db.delete_unique('userprofile_uservote', ['user_id', 'voting_id'])

        # Adding unique constraint on 'UserVote', fields ['user', 'id']
        db.create_unique('userprofile_uservote', ['user_id', 'id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'riksdagen.document': {
            'Meta': {'object_name': 'Document'},
            'committee_prop_url_xml': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'doc_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'doctype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'doctype2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'document_url_html': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'document_url_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'documentstatus_url_xml': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'govorgan': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hangar_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'htmlformat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party_year': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'publicised': ('django.db.models.fields.DateTimeField', [], {}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'related_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'serial_num': ('django.db.models.fields.IntegerField', [], {}),
            'serial_num_end': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sourceid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'system_date': ('django.db.models.fields.DateTimeField', [], {}),
            'templabel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'riksdagen.person': {
            'Meta': {'object_name': 'Person'},
            'born_year': ('django.db.models.fields.IntegerField', [], {}),
            'constituency': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'intressent_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'iort': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'userprofile.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_voted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'nr_votes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'open_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'related_name': "'profile'", 'unique': 'True'})
        },
        'userprofile.usersimilarity': {
            'Meta': {'object_name': 'UserSimilarity'},
            'common_votes': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riksdagen.Person']", 'related_name': "'user_similarity'"}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'similarity'"})
        },
        'userprofile.uservote': {
            'Meta': {'object_name': 'UserVote', 'unique_together': "(('user', 'voting_id'),)"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_voted': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'doc_item': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riksdagen.Document']", 'related_name': "'userdoc_votes'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party_year': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pertaining': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'votes'"}),
            'vote': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'voting_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'voting_part': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['userprofile']