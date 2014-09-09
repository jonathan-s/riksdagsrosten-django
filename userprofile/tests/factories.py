import datetime

from django.contrib.auth.models import User
import factory


from ..models import UserVote
from ..models import UserProfile
from riksdagen.tests.factories import DocumentFactory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "User-{}".format(n))
    password = 'pass'


class UserProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    open_profile = True
    nr_votes = 0
    last_voted_on = datetime.date(2000, 1, 1)

class UserVoteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserVote

    user = factory.SubFactory(UserFactory)
    document = factory.SubFactory(DocumentFactory)

    voting_id = factory.sequence(lambda n: 'AAFAC7F5-AFCD-11D8-AE5D-000475{}D1'.format(1000+n))
    party_year = factory.SelfAttribute('document.party_year')
    label = factory.SelfAttribute('document.label')
    doc_item = 1
    vote = 'Ja'
    pertaining = 'sakfrågan'
    voting_part = 'huvud'
    date = datetime.date(2014, 1, 1)
