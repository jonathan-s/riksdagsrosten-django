# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('riksdagen_person', (
            ('intressent_id', self.gf('django.db.models.fields.CharField')(max_length=128, primary_key=True)),
            ('born_year', self.gf('django.db.models.fields.IntegerField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('sort_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('iort', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('party', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('constituency', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('riksdagen', ['Person'])

        # Adding model 'PersonCommitment'
        db.create_table('riksdagen_personcommitment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organ_kod', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('role_code', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('seq_nr', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('until', self.gf('django.db.models.fields.DateField')()),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('commitment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riksdagen.Person'], related_name='commitments')),
        ))
        db.send_create_signal('riksdagen', ['PersonCommitment'])

        # Adding model 'PersonalRecord'
        db.create_table('riksdagen_personalrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('record', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('f_record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riksdagen.Person'], related_name='records')),
        ))
        db.send_create_signal('riksdagen', ['PersonalRecord'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('riksdagen_person')

        # Deleting model 'PersonCommitment'
        db.delete_table('riksdagen_personcommitment')

        # Deleting model 'PersonalRecord'
        db.delete_table('riksdagen_personalrecord')


    models = {
        'riksdagen.person': {
            'Meta': {'object_name': 'Person'},
            'born_year': ('django.db.models.fields.IntegerField', [], {}),
            'constituency': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'intressent_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'iort': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sort_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'riksdagen.personalrecord': {
            'Meta': {'object_name': 'PersonalRecord'},
            'f_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riksdagen.Person']", 'related_name': "'records'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'record_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'riksdagen.personcommitment': {
            'Meta': {'object_name': 'PersonCommitment'},
            'commitment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riksdagen.Person']", 'related_name': "'commitments'"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organ_kod': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'role_code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'seq_nr': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'until': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['riksdagen']