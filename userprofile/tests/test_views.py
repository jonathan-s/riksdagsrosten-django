# encoding: utf-8

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.management import call_command
from django.contrib.auth.models import User

from .factories import UserProfileFactory
from .factories import UserVoteFactory
from riksdagen.tests.factories import VotingFactory
from riksdagen.tests.factories import VotingAggFactory

from userprofile.views import userprofile
from userprofile.views import openprofile
from userprofile.views import poll_detail_vote
from userprofile.models import UserVote
from userprofile.models import UserSimilarity
from userprofile.models import UserProfile
from riksdagen.models import Voting

def setUpModule():
    call_command('loaddata', 'riksdagsrosten/init_facebook_app.json', verbosity=0)

class UserprofileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='joe', password='mupp')
        UserProfileFactory(user=self.user)
        VotingFactory.create_batch(6)
        # creates 5 different users as well.
        for v in Voting.objects.all():
            UserVoteFactory(
                document=v.document,
                voting_id=v.voting_id,
                user=self.user
            )

    def test_userprofile_resolves_url_correct(self):
        found = resolve('/profil/')

        self.assertEqual(found.func, userprofile)

    def test_userprofile_has_template(self):
        self.client.login(username='joe', password='mupp')
        response = self.client.get('/profil/', follow=True)

        self.assertTemplateUsed(response, 'userprofile.html')

    def test_userprofile_needs_logged_in_user(self):
        response = self.client.get('/profil/', follow=True)

        # TODO, change to another login page.
        self.assertNotEqual(response.request['PATH_INFO'], '/profil/')
        self.assertEqual(response.request['PATH_INFO'], '/accounts/login/')

    def test_userprofile_has_context(self):
        self.client.login(username='joe', password='mupp')
        response = self.client.get('/profil/')

        votes = UserVote.objects.filter(user__pk=self.user.pk)[:5]
        similarity = UserSimilarity.objects.filter(user__pk=self.user.pk)[:5]

        self.assertEqual(list(response.context['votes']), list(votes))
        self.assertEqual(list(response.context['similarity']), list(similarity))
        self.assertEqual(response.context['user'].profile.nr_votes, 6)

class OpenprofileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='joe', password='schmoe')
        self.profile = UserProfileFactory(user=self.user, open_profile=True)

    def test_openprofile_resolves_url_correct(self):
        found = resolve('/anvandare/{}/'.format(self.user.username))

        self.assertEqual(found.func, openprofile)
        self.assertEqual(found.kwargs['username'], 'joe')

    def test_openprofile_has_template(self):
        response = self.client.get('/anvandare/{}/'.format(self.user.username))

        self.assertTemplateUsed(response, 'userprofile.html')

    def test_openprofile_not_working_if_closed(self):
        self.profile.open_profile = False
        self.profile.save()

        response = self.client.get('/anvandare/{}/'.format(self.user.username))

        self.assertEqual(response.status_code, 404)

    def test_openprofile_not_working_for_empty_user(self):
        response = self.client.get('/anvandare/no_user/')

        self.assertEqual(response.status_code, 404)

    def test_openprofile_has_context(self):
        VotingFactory.create_batch(6)
        # creates 5 different users as well.
        for v in Voting.objects.all():
            UserVoteFactory(
                document=v.document,
                voting_id=v.voting_id,
                user=self.user
            )

        response = self.client.get('/anvandare/{}/'.format(self.user.username))

        votes = UserVote.objects.filter(user__username=self.user.username)[:5]
        similarity = UserSimilarity.objects.filter(user__username=self.user.username)[:5]

        self.assertEqual(list(response.context['votes']), list(votes))
        self.assertEqual(list(response.context['similarity']), list(similarity))
        self.assertEqual(response.context['userprofile'].nr_votes, 6)

class PollDetailVoteTest(TestCase):
    def setUp(self):
        self.v = VotingAggFactory(
            document__doc_id='GY01AU1',
            q1_yes=10,
            q1_no=290)

        VotingFactory(document=self.v.document, doc_item=1)

        self.user = User.objects.create_user(username='joe', password='pass')

    def test_voteview_resolves_url_correct(self):
        found = resolve('/votering/{0}/1/Ja/'.format(self.v.document.doc_id))

        self.assertEqual(found.func, poll_detail_vote)

    def test_voteview_needs_logged_in_user(self):
        response = self.client.get('/votering/{}/1/Ja/'.format(self.v.document.doc_id))

        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_voteview_only_accepts_ja_nej(self):
        response = self.client.get('/votering/{}/1/eja/'.format(self.v.document.doc_id))

        self.assertEqual(response.status_code, 404)

    def test_voteview_redirects_after_vote(self):
        self.client.login(username='joe', password='pass')
        response = self.client.get('/votering/{}/1/Ja/'.format(self.v.document.doc_id))

        self.assertEqual(response.status_code, 302)

    def test_voteview_redirects_to_doc_id(self):
        self.client.login(username='joe', password='pass')
        response = self.client.get('/votering/{}/1/Ja/'.format(self.v.document.doc_id))

        self.assertEqual(response.url, 'http://testserver/votering/{}'.format(self.v.document.doc_id))

    def test_voteview_make_a_vote_for_user(self):
        self.client.login(username='joe', password='pass')
        response = self.client.get('/votering/{}/1/Ja/'.format(self.v.document.doc_id))

        vote = UserVote.objects.get(user=self.user)
        self.assertEqual(vote.vote, 'Ja')
