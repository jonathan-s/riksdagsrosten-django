from datetime import date

from django.contrib.auth.models import User
import factory


from ..models import UserVote
from ..models import UserProfile

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
    last_voted_on = date(2000, 1, 1)

    # needs more data