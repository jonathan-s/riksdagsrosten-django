from datetime import date
from unittest import skip

from django.test import TestCase
from django.contrib.auth.models import User

from .factories import UserProfileFactory
from .factories import UserVoteFactory
from userprofile.models import UserProfile
from userprofile.models import UserSimilarity
from riksdagen.tests.factories import VotingFactory
from riksdagen.tests.factories import PersonWithCommitment
from riksdagen.tests.factories import PersonFactory
from riksdagen.models import Person
from riksdagen.models import Voting

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

    def test_save_uservote_only_generates_similarity_for_mps_parliament(self):
        v = UserVoteFactory(user=self.user)
        PersonWithCommitment.create_batch(2)
        PersonFactory.create_batch(2)
        for p in Person.objects.all():
            VotingFactory(voting_id=v.voting_id, fk_voting_person=p)
        v.save()

        qualified_votes = UserSimilarity.objects.filter().count()
        nr_of_total_mps = Person.objects.all().count()

        self.assertEqual(qualified_votes, 2)
        self.assertEqual(nr_of_total_mps, 4)


    def test_save_uservote_usersimilarity_is_correct(self):
        v1 = UserVoteFactory(user=self.user, vote='Ja')
        v2 = UserVoteFactory(user=self.user, vote='Ja')
        PersonWithCommitment.create_batch(2)

        mp1 = Person.objects.all()[0]
        mp2 = Person.objects.all()[1]

        VotingFactory(voting_id=v1.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v1.voting_id, fk_voting_person=mp2, vote='Nej')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp2, vote='Ja')

        v1.save() # gotcha that it needs to be saved to generate similarity

        mp1_similarity = UserSimilarity.objects.get(mp__pk=mp1.intressent_id)
        mp2_similarity = UserSimilarity.objects.get(mp__pk=mp2.intressent_id)

        self.assertEqual(mp1_similarity.percentage, 100)
        self.assertEqual(mp2_similarity.percentage, 50)

    def test_save_uservote_similarity_works_for_non_existing_votes(self):
        v1 = UserVoteFactory(user=self.user, vote='Ja')
        v2 = UserVoteFactory(user=self.user, vote='Ja')
        PersonWithCommitment.create_batch(2)

        mp1 = Person.objects.all()[0]
        mp2 = Person.objects.all()[1]

        VotingFactory(voting_id=v1.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp2, vote='Nej')
        # mp2 has a missing vote here, should not generate error

        v1.save() # gotcha that it needs to be saved to generate similarity

        mp1_similarity = UserSimilarity.objects.get(mp__pk=mp1.intressent_id)
        mp2_similarity = UserSimilarity.objects.get(mp__pk=mp2.intressent_id)

        self.assertEqual(mp1_similarity.percentage, 100)
        self.assertEqual(mp2_similarity.percentage, 0)
        self.assertEqual(mp2_similarity.common_votes, 1)

    def test_similarity_does_not_take_into_account_absence_or_abstained(self):
        v1 = UserVoteFactory(user=self.user, vote='Ja')
        v2 = UserVoteFactory(user=self.user, vote='Ja')
        PersonWithCommitment.create_batch(2)

        mp1 = Person.objects.all()[0]
        mp2 = Person.objects.all()[1]

        VotingFactory(voting_id=v1.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp1, vote='Ja')
        VotingFactory(voting_id=v1.voting_id, fk_voting_person=mp2, vote='Nej')
        VotingFactory(voting_id=v2.voting_id, fk_voting_person=mp2, vote='Frånvarande')

        v1.save() # gotcha that it needs to be saved to generate similarity

        mp1_similarity = UserSimilarity.objects.get(mp__pk=mp1.intressent_id)
        mp2_similarity = UserSimilarity.objects.get(mp__pk=mp2.intressent_id)

        self.assertEqual(mp1_similarity.percentage, 100)
        self.assertEqual(mp2_similarity.percentage, 0)
        self.assertEqual(mp2_similarity.common_votes, 1)

class UserProfileTest(TestCase):

    def test_userprofile_gets_created_automatically_with_newuser(self):
        u = User.objects.create_user(username='joe', password='pass')

        profile = UserProfile.objects.get(user=u)

        self.assertEqual(profile.user, u)

class UserSimilarityTest(TestCase):
    # TODO
    def test_user_and_mp_is_unique(self):
        pass
