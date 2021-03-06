import datetime

import factory

from riksdagen.models import Person, PersonCommitment, PersonalRecord
from riksdagen.models import Voting, Document, VotingAgg

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

class DocumentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Document

    doc_id = factory.Sequence(lambda n: 'GY01AU{}'.format(n))
    hangar_id = factory.Sequence(lambda n: 2000+n)
    party_year = '2013/14'
    label = factory.Sequence(lambda n: 'FIU{}'.format(n))
    doctype = 'bet'
    doctype2 = 'bet'
    subtype = 'bet'
    templabel = ''
    govorgan = 'FIU'
    receiver = ''
    serial_num = 4
    serial_num_end = 0
    date = datetime.date(2014, 6, 22)
    system_date = datetime.datetime(2014, 6, 22)
    publicised = datetime.datetime(2014, 6, 22)
    title = factory.sequence(lambda n: 'Random Junk Title {}'.format(n))
    subtitle = ''
    status = ''
    related_id = ''
    source = ''
    sourceid = ''
    htmlformat = ''
    document_url_text = 'http://data.riksdagen.se/dokument/GY01AU4/text'
    document_url_html = 'Lots of html'
    documentstatus_url_xml = 'http://data.riksdagen.se/dokumentstatus/GY01AU4'
    committee_prop_url_xml = 'http://data.riksdagen.se/utskottsforslag/GY01AU4'
    html = """<html><body>
            <a href=""></a><p></p><p></p><p></p>
            <a href=""></a><p></p><p></p><p></p>
            <a href=""></a><p></p><p></p><p></p></body></html>"""
    summary = ''


class VotingAggFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = VotingAgg

    document = factory.SubFactory(DocumentFactory)
    voting_id = factory.sequence(lambda n: 'AAFAC7F5-AFCD-11D8-AE5D-000475{}D1'.format(1000+n))
    date = datetime.date(2014, 6, 17)
    u_q1_yes = 0
    u_q1_no = 0
    q1_yes = 0
    q1_no = 0
    q1_absent = 0
    q1_abstained = 0


class VotingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Voting

    desk_nr = 1
    voting_id = factory.sequence(lambda n: 'AAFAC7F5-AFCD-11D8-AE5D-000475{}D1'.format(1000+n))
    party_year = factory.SelfAttribute('document.party_year')
    label = factory.SelfAttribute('document.label')
    doc_item = 1
    vote = 'Ja'
    pertaining = 'sakfrågan'
    voting_part = 'huvud'
    date = datetime.date(2014, 1, 1)

    #random facts
    parti = factory.SelfAttribute('fk_voting_person.party')
    namn = factory.SelfAttribute('fk_voting_person.sort_name')
    valkrets = 'random county'
    valkretsnummer = '1'
    iort = ''
    fornamn = factory.SelfAttribute('fk_voting_person.firstname')
    efternamn = factory.SelfAttribute('fk_voting_person.lastname')
    kon = factory.SelfAttribute('fk_voting_person.sex')
    fodd = factory.SelfAttribute('fk_voting_person.born_year')

    document = factory.SubFactory(DocumentFactory)
    fk_voting_person = factory.SubFactory(PersonFactory)



