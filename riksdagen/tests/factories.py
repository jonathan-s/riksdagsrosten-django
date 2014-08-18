import datetime

import factory

from riksdagen.models import Person, PersonCommitment, PersonalRecord
from riksdagen.models import Voting, Document

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    intressent_id = factory.Sequence(lambda n: '0' + str(449003924218 + n) )
    born_year = 1985
    sex = 'Man'
    lastname = 'Riksdagsman'
    firstname = factory.Sequence(lambda n: "Leonard-{0}".format(n))
    sort_name = factory.Sequence(lambda n: 'Riksdagsman, Leonard-{0}'.format(n))
    iort = ''
    party = 'M'
    constituency = 'Dalarna'
    status = 'Tidigare riksdagsledamot'


class PersonCommitmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonCommitment

    organ_kod = 'kam'
    role_code = 'Riksdagsledamot'
    seq_nr = 51
    status = 'Ledig'
    type_of = 'kammaruppdrag'
    from_date = datetime.date(2010, 10, 4)
    until = datetime.date(2014, 9, 29)
    task = 'Jessica Rosencrantz 2010-10-04 - 2010-10-18'
    fk_personcommitment_person = factory.SubFactory(PersonFactory)


class PersonWithCommitment(PersonFactory):

    commitments = factory.RelatedFactory(PersonCommitmentFactory, 'fk_personcommitment_person')


class PersonalRecordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonalRecord

    record_name = 'sv'
    record = 'Civilekonom'
    record_type = 'titlar'
    fk_personcommitment_person = factory.SubFactory(PersonFactory)

class VotingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Voting

    fk_voting_person = factory.Sequence(lambda n: '0' + str(449003924218 + n) )
    hangar_id = 123123

    voting_id = 'AAFAC7F5-AFCD-11D8-AE5D-0004755038D1'
    party_year = '2013/14'
    label = 'FIU21'
    doc_item = 1
    vote = 'Ja'
    pertaining = 'sakfrågan'
    voting_part = 'huvud'
    desk_nr = 25
    date = datetime.date(2014, 6, 17)

    parti = 'M'
    namn = factory.Sequence(lambda n: "Leonard-{0}".format(n))
    valkrets = 'Stockholms kommun'
    efternamn = 'Riksdagsman'
    namn = factory.Sequence(lambda n: "Leonard-{0}".format(n))
    kon = 'man'
    fodd = 1985

class DocumentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Document

    doc_id = 'GY01AU4'
    hangar_id = 123123
    party_year = '2013/14'
    label = 'FIU21'
    doctype = 'bet'
    doctype2 = 'bet'
    subtype = 'bet'
    temblabel = ''
    govorgan = 'FIU'
    receiver = ''
    serial_num = 4
    serial_num_end = 0
    date = datetime.date(2014, 6, 22)
    system_date = datetime.datetime(2014, 6, 22)
    publicised = datetime.datetime(2014, 6, 22)
    title = 'Random Junk Title'
    subtitle = ''
    q1_yes = 0
    q1_no = 0
    q1_absent = 0
    q1_abstained = 0
    status = ''
    related_id = ''
    source = ''
    sourceid = ''
    htmlformat = ''
    document_url_text = 'http://data.riksdagen.se/dokument/GY01AU4/text'
    document_url_html = 'Lots of html'
    documentstatus_url_xml = 'http://data.riksdagen.se/dokumentstatus/GY01AU4'
    committee_prop_url_xml = 'http://data.riksdagen.se/utskottsforslag/GY01AU4'
    html = 'Again lots of html'




