import datetime

import factory

from riksdagen.models import Person, PersonCommitment, PersonalRecord

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

