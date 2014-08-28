# -*- coding: utf-8 -*-

from datetime import date

from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver


"""All the mappings can be found in rename.py in data"""

class Person(models.Model):
    intressent_id = models.CharField(max_length=128, primary_key=True)
    born_year = models.IntegerField()
    sex = models.CharField(max_length=10)
    lastname = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)
    sort_name = models.CharField(max_length=60)
    iort = models.CharField(max_length=60)
    party = models.CharField(max_length=30)
    constituency = models.CharField(max_length=60)
    status = models.CharField(max_length=60)

    def __str__(self):
        return "{0} {1} ({2})".format(self.firstname, self.lastname, self.party)

class PersonCommitment(models.Model):
    organ_kod = models.CharField(max_length=50)
    role_code = models.CharField(max_length=60)
    seq_nr = models.IntegerField()
    status = models.CharField(max_length=60)
    type_of = models.CharField(max_length=60)
    from_date = models.DateField()
    until = models.DateField()
    task = models.CharField(max_length=400)
    fk_personcommitment_person = models.ForeignKey(Person, related_name='commitments')

    def __str__(self):
        return "{0} för {1}".format(self.role_code, self.task)


class PersonalRecord(models.Model):
    record_name = models.CharField(max_length=60)
    record = models.CharField(max_length=200)
    record_type = models.CharField(max_length=60)
    fk_personalrecord_person = models.ForeignKey(Person, related_name='records')

    def __str__(self):
        return "{0}: {1}".format(self.record_name, self.record)


class VotingBase(models.Model):
    voting_id = models.CharField(max_length=255, db_index=True)
    party_year = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    doc_item = models.IntegerField(db_index=True) #
    vote = models.CharField(max_length=255, db_index=True)
    pertaining = models.CharField(max_length=255)
    voting_part = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        abstract = True


class Voting(VotingBase):
    document = models.ForeignKey('Document', db_column='hangar_id', related_name='doc_votes')
    fk_voting_person = models.ForeignKey(Person, related_name='votes')

    desk_nr = models.CharField(max_length=255)
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

class VotingAgg(models.Model):
    document = models.ForeignKey('Document', db_column='hangar_id', related_name='voting_agg')
    voting_id = models.CharField(max_length=255)
    date = models.DateField()
    q1_yes = models.IntegerField()
    q1_no = models.IntegerField()
    q1_absent = models.IntegerField()
    q1_abstained = models.IntegerField()


class Document(models.Model):
    hangar_id = models.IntegerField(primary_key=True)
    doc_id = models.CharField(max_length=100, db_index=True)
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

def votes(value_list, hgid):
    """Takes hangar_id, orders by doc_item, takes the first
        elements doc_item and gets the vote results of that"""

    qs = Voting.objects.filter(document_id__exact=hgid,
        pertaining__exact='sakfrågan').order_by('doc_item')
    if qs.exists():
        doc_item = qs[0].doc_item
        d = {v[1]: qs.filter(vote__exact='{0}'.format(v[0]),
                doc_item=doc_item).count() for v in value_list}
        d['voting_id'] = qs[0].voting_id
        d['date'] = qs[0].date
    else:
        d = {}
    return d

def update_or_create(updated_values, hgid):
    instance, created = VotingAgg.objects.get_or_create(**updated_values)
    if created:
        pass # no need to do anything
    else:
        VotingAgg.objects.update(**updated_values)

@receiver(post_save, sender=Document)
def update_votes(sender, instance, created, raw, using, update_fields, **kwargs):
    hgid = instance.hangar_id
    d = votes([
            ('Ja', 'q1_yes'), ('Nej', 'q1_no'),
            ('Frånvarande', 'q1_absent'),
            ('Avstår', 'q1_abstained')], hgid)
    if d.get('voting_id'):
        d['document'] = instance
        update_or_create(d, hgid)


