from datetime import date

from django.test import TestCase

from riksdagen.tests.factories import PersonFactory
from riksdagen.tests.factories import DocumentFactory
from .factories import UserProfileFactory
from userprofile.models import UserVote
from userprofile.models import UserProfile


class UserProfileTest(TestCase):

    def setUp(self):
        self.doc = DocumentFactory()
        self.person = PersonFactory()
        self.user = UserProfileFactory(nr_votes=0)
        self.vote = UserVote.objects.create(user=self.user.user, document=self.doc)

    def test_userprofile_vote_increase_by_one(self):
        user = UserProfile.get(self.user.id)

        self.assertEqual(user.nr_votes, 1)

    def test_userprofile_changes_last_voted_on(self):
        user = UserProfile.get(self.user.id)

        self.assertEqual(user.last_voted_on.date(), date.today())





