# -*- coding: utf-8 -*-

from datetime import date

from django.db import models


"""
MAPPING
Person -> Person

intressent_id -> intressent_id
född_år -> born_year
kön -> sex
efternamn -> lastname
tilltalsnamn -> firstname
sorteringsnamn -> sort_name
iort -> iort
parti -> party
valkrets -> constituency
status -> status

Missing picture urls in person.sql
"""


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

"""
MAPPING
personuppgift -> PersonalRecord

uppgift_kod -> record_name
uppgift -> record
uppgift_typ -> record_type
intressent_id -> FK_personalrecord_person

"""

class PersonalRecord(models.Model):
    record_name = models.CharField(max_length=60)
    record = models.CharField(max_length=60)
    record_type = models.CharField(max_length=60)
    FK_personalrecord_person = models.ForeignKey(Person, related_name='records')

    def __str__(self):
        return "{0}: {1}".format(self.record_name, self.record)



