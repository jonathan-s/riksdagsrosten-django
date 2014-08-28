from datetime import date
from unittest import skip

from django.test import TestCase

from .factories import UserProfileFactory
from .factories import UserVoteFactory
from userprofile.models import UserProfile
from userprofile.models import UserSimilarity
from riksdagen.tests.factories import VotingFactory


class UserVoteTest(TestCase):

    def setUp(self):
        self.userprofile = UserProfileFactory(nr_votes=0)
        self.user = self.userprofile.user

    def test_save_uservote_increase_userprofile_vote(self):
        UserVoteFactory(user=self.user)

        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.nr_votes, 1)

    def test_save_uservote_userprofile_changes_last_voted_on(self):
        UserVoteFactory(user=self.user)

        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.last_voted_on.date(), date.today())


