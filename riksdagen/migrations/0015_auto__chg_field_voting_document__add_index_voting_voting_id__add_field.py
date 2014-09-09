# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Voting.document'
        db.alter_column('riksdagen_voting', 'hangar_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riksdagen.Document'], db_column='hangar_id'))
        # Adding index on 'Voting', fields ['voting_id']
        db.create_index('riksdagen_voting', ['voting_id'])

        # Adding field 'VotingAgg.u_q1_yes'
        db.add_column('riksdagen_votingagg', 'u_q1_yes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'VotingAgg.u_q1_no'
        db.add_column('riksdagen_votingagg', 'u_q1_no',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'VotingAgg.document'
        db.alter_column('riksdagen_votingagg', 'hangar_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['riksdagen.Document'], db_column='hangar_id'))
        # Adding unique constraint on 'VotingAgg', fields ['document']
        db.create_unique('riksdagen_votingagg', ['hangar_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'VotingAgg', fields ['document']
        db.delete_unique('riksdagen_votingagg', ['hangar_id'])

        # Removing index on 'Voting', fields ['voting_id']
        db.delete_index('riksdagen_voting', ['voting_id'])

         # Changing field 'Voting.document'
        db.alter_column('riksdagen_voting', 'document_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riksdagen.Document']))
        # Deleting field 'VotingAgg.u_q1_yes'
        db.delete_column('riksdagen_votingagg', 'u_q1_yes')

        # Deleting field 'VotingAgg.u_q1_no'
        db.delete_column('riksdagen_votingagg', 'u_q1_no')


        # Changing field 'VotingAgg.document'
        db.alter_column('riksdagen_votingagg', 'document_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['riksdagen.Document']))

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
            'intressent_id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '128'}),
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
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['riksdagen.Document']", 'related_name': "'doc_votes'", 'db_column': "'hangar_id'"}),
            'efternamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fk_voting_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': "orm['riksdagen.Person']"}),
            'fodd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fornamn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'voting_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'voting_part': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'riksdagen.votingagg': {
            'Meta': {'object_name': 'VotingAgg'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'document': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['riksdagen.Document']", 'related_name': "'voting_agg'", 'db_column': "'hangar_id'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q1_absent': ('django.db.models.fields.IntegerField', [], {}),
            'q1_abstained': ('django.db.models.fields.IntegerField', [], {}),
            'q1_no': ('django.db.models.fields.IntegerField', [], {}),
            'q1_yes': ('django.db.models.fields.IntegerField', [], {}),
            'u_q1_no': ('django.db.models.fields.IntegerField', [], {}),
            'u_q1_yes': ('django.db.models.fields.IntegerField', [], {}),
            'voting_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['riksdagen']