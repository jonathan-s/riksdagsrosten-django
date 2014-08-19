# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VotingAgg'
        db.create_table('riksdagen_votingagg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voting_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hangar_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('q1_yes', self.gf('django.db.models.fields.IntegerField')()),
            ('q1_no', self.gf('django.db.models.fields.IntegerField')()),
            ('q1_absent', self.gf('django.db.models.fields.IntegerField')()),
            ('q1_abstained', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('riksdagen', ['VotingAgg'])

        # Deleting field 'Document.q1_absent'
        db.delete_column('riksdagen_document', 'q1_absent')

        # Deleting field 'Document.q1_no'
        db.delete_column('riksdagen_document', 'q1_no')

        # Deleting field 'Document.q1_abstained'
        db.delete_column('riksdagen_document', 'q1_abstained')

        # Deleting field 'Document.q1_yes'
        db.delete_column('riksdagen_document', 'q1_yes')


    def backwards(self, orm):
        # Deleting model 'VotingAgg'
        db.delete_table('riksdagen_votingagg')

        # Adding field 'Document.q1_absent'
        db.add_column('riksdagen_document', 'q1_absent',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.q1_no'
        db.add_column('riksdagen_document', 'q1_no',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.q1_abstained'
        db.add_column('riksdagen_document', 'q1_abstained',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Document.q1_yes'
        db.add_column('riksdagen_document', 'q1_yes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
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
            'hangar_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'htmlformat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        'riksdagen.personalrecord': {
            'Meta': {'object_name': 'PersonalRecord'},
            'fk_personalrecord_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': "orm['riksdagen.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'record_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'riksdagen.personcommitment': {
            'Meta': {'object_name': 'PersonCommitment'},
            'fk_personcommitment_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commitments'", 'to': "orm['riksdagen.Person']"}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organ_kod': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role_code': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'seq_nr': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'type_of': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'until': ('django.db.models.fields.DateField', [], {})
        },
        'riksdagen.voting': {
            'Meta': {'object_name': 'Voting'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'desk_nr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'doc_item': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'hangar_id'", 'related_name': "'doc_votes'", 'to_field': "'hangar_id'", 'to': "orm['riksdagen.Document']"}),
            'efternamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fk_voting_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': "orm['riksdagen.Person']"}),
            'fodd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fornamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hangar_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iort': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'kon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'namn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parti': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party_year': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pertaining': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valkrets': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valkretsnummer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vote': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'voting_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voting_part': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'riksdagen.votingagg': {
            'Meta': {'object_name': 'VotingAgg'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'hangar_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q1_absent': ('django.db.models.fields.IntegerField', [], {}),
            'q1_abstained': ('django.db.models.fields.IntegerField', [], {}),
            'q1_no': ('django.db.models.fields.IntegerField', [], {}),
            'q1_yes': ('django.db.models.fields.IntegerField', [], {}),
            'voting_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'riksdagen.votingdistinct': {
            'Meta': {'object_name': 'VotingDistinct', 'managed': 'False', 'db_table': "'riksdagen_voting_distinct'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'desk_nr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'doc_item': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'hangar_id'", 'related_name': "'ddoc_votes'", 'to_field': "'hangar_id'", 'to': "orm['riksdagen.Document']"}),
            'efternamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fk_voting_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vd_votes'", 'to': "orm['riksdagen.Person']"}),
            'fodd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fornamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hangar_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iort': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'kon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'namn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parti': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party_year': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pertaining': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valkrets': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valkretsnummer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vote': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'voting_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voting_part': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['riksdagen']