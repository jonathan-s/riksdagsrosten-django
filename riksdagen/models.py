# -*- coding: utf-8 -*-

from datetime import date

from django.db import models

"""All the mappings can be found in rename.py in data"""

class Person(models.Model):
    intressent_id = models.CharField(max_length=128, primary_key=True)
    born_year = models.IntegerField()
    sex = models.CharField(max_length=10)
    lastname = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    sort_name = models.CharField(max_length=60)
    iort = models.CharField(max_length=60)
    party = models.CharField(max_length=3)
    constituency = models.CharField(max_length=60)
    status = models.CharField(max_length=60)

    def __str__(self):
        return "{0} {1} ({2})".format(self.firstname, self.lastname, self.party)

<<<<<<< HEAD
"""
MAPPING
personuppdrag -> PersonCommitment

organ_kod -> organ_kod
roll_kod -> role_code
ordningsnummer -> seq_nr
status -> status
typ -> type
from -> from_date
tom -> until
uppgift -> task
intressent_id -> FK_personcommitment_person

"""
=======
>>>>>>> 4b01168... Removed spec from models and added voting model + small todo in views

class PersonCommitment(models.Model):
    organ_kod = models.CharField(max_length=10)
    role_code = models.CharField(max_length=30)
    seq_nr = models.IntegerField()
    status = models.CharField(max_length=60)
    from_date = models.DateField()
    until = models.DateField()
    task = models.CharField(max_length=60)
    FK_personcommitment_person = models.ForeignKey(Person, related_name='commitments')

    def __str__(self):
        return "{0} för {1}".format(self.role_code, self.task)


class PersonalRecord(models.Model):
    record_name = models.CharField(max_length=60)
    record = models.CharField(max_length=60)
    record_type = models.CharField(max_length=60)
    FK_personalrecord_person = models.ForeignKey(Person, related_name='records')

    def __str__(self):
        return "{0}: {1}".format(self.record_name, self.record)

class Voting(models.Model):
    hangar_id = models.IntegerField() # a many to many field ?
    voting_id = models.CharField(max_length=255)
    party_year = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    doc_item = models.IntegerField(db_index=True)
    fk_voting_person = models.ForeignKey(Person, related_name='votes')
    vote = models.CharField(max_length=255, db_index=True)
    pertaining = models.CharField(max_length=255)
    voting_part = models.CharField(max_length=255)
    desk_nr = models.CharField(max_length=255)
    date = models.DateField()
    # fields below not used, but included for completeness
    # and because it makes it easy to import data.
    namn = models.CharField(max_length=255)
    parti = models.CharField(max_length=255)
    valkrets = models.CharField(max_length=255)
    valkretsnummer = models.CharField(max_length=255)
    iort = models.CharField(max_length=255)
    fornamn = models.CharField(max_length=255)
    efternamn = models.CharField(max_length=255)
    kon = models.CharField(max_length=255)
    fodd = models.CharField(max_length=255)

    def __str__(self):
        return "{0}:{1} Röst: {2}".format(
            self.party_year, self.label, self.vote)

class Document(models.Model):
    # doc_id should be primary key
    doc_id = models.CharField(max_length=100, db_index=True)
    hangar_id = models.IntegerField(db_index=True)
    party_year = models.CharField(max_length=30)
    label = models.CharField(max_length=100)
    doctype = models.CharField(max_length=100)
    doctype2 = models.CharField(max_length=100)
    subtype = models.CharField(max_length=100)
    templabel = models.CharField(max_length=100)
    govorgan = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    serial_num = models.IntegerField()
    serial_num_end = models.IntegerField()
    date = models.DateField()
    system_date = models.DateTimeField()
    publicised = models.DateTimeField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    q1_yes = models.IntegerField()
    q1_no = models.IntegerField()
    q1_absent = models.IntegerField()
    q1_abstained = models.IntegerField()
    status = models.CharField(max_length=255)
    related_id = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    sourceid = models.CharField(max_length=255)
    htmlformat = models.CharField(max_length=255)
    document_url_text = models.CharField(max_length=255)
    document_url_html = models.CharField(max_length=255)
    documentstatus_url_xml = models.CharField(max_length=255)
    committee_prop_url_xml = models.CharField(max_length=255)
    html = models.TextField()

    def __str__(self):
        return "{0}:{1} :{2}".format(
            self.party_year, self.label, self.title)








