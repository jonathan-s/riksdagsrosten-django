# encoding: utf-8

from datetime import date
from unittest import skip

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.management import call_command
from django.shortcuts import get_object_or_404

from .factories import PersonFactory, PersonWithCommitment
from .factories import VotingAggFactory
from riksdagen.constants import GOVORGAN, PARTY_NAME
from riksdagen.views import party, partywithname, singlemp
from riksdagen.views import allmp, polls
from riksdagen.models import Person, VotingAgg

"""

import logging
logger = logging.getLogger('factory')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
"""

def setUpModule():
    call_command('loaddata', 'riksdagen/tests/init_facebook_app.json', verbosity=0)

class PollsTest(TestCase):

    def setUp(self):
        VotingAggFactory()
        self.d = VotingAgg.objects.select_related('document').order_by('-date')

    def test_polls_resolves_url_correct(self):
        found = resolve('/votering/tidigare/kategori/')

        self.assertEqual(found.func, polls)

    def test_polls_has_right_context(self):
        response = self.client.get('/votering/tidigare/kategori', follow=True)

        self.assertEqual(list(response.context['documents']), list(self.d))
        self.assertEqual(response.context['govorgan'], GOVORGAN)

class PartyTest(TestCase):

    def test_party_resolves_url_correct(self):
        found = resolve('/parti/')

        self.assertEqual(found.func, party)

    def test_has_right_number_of_mps(self):
        PersonWithCommitment.create_batch(10,
            party='S', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='S', commitments__until=date(2014, 9, 1))
        PersonWithCommitment(party='S', commitments__role_code='Something else')
        response = self.client.get('/parti/')

        self.assertEqual(response.context['party_name'], PARTY_NAME)
        self.assertEqual(response.context['counts']['socialdemokraterna'], 10)

class PartyWithNameTest(TestCase):

    def test_partyname_resolves_url_correct(self):
        found = resolve('/parti/M/')

        self.assertEqual(found.func, partywithname)
        self.assertEqual(found.kwargs, {'partyname': 'M'})

    def test_partyname_correct_template(self):
        response = self.client.get('/parti/moderaterna/')

        self.assertTemplateUsed(response, 'party-mp.html')

    def test_partyname_has_correct_mps(self):
        PersonWithCommitment(party='M', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='S', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='M', commitments__until=date(2014, 1, 1))
        #Above should not be in list.
        response = self.client.get('/parti/moderaterna/')

        mps = Person.objects.filter(
            party__iexact='M', commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')
        self.assertEqual(list(response.context['mps']), list(mps))

    def test_party_returns_response(self):
        response = self.client.get('/parti/moderaterna/')

        self.assertEqual(response.status_code, 200)

class SingleMpTest(TestCase):

    def setUp(self):
        self.person = PersonFactory()

    def test_singlemp_resolves_url_correct(self):
        found = resolve('/ledamot/123123/name-here/')
        found2 = resolve('/ledamot/123123/')

        self.assertEqual(found.func, singlemp)
        self.assertEqual(found2.func, singlemp)

    def test_singlemp_redirects_correctly(self):
        response = self.client.get('/ledamot/%s/' % self.person.intressent_id)

        self.assertEqual(response.status_code, 301)

    def test_singlemp_has_correct_template(self):
        idnr = self.person.intressent_id
        nameslug = "{0}-{1}".format(self.person.firstname, self.person.lastname)
        response = self.client.get('/ledamot/{0}/{1}/'.format(idnr, nameslug))

        self.assertTemplateUsed(response, 'mp.html')

    def test_404_works_properly(self):
        response = self.client.get('/ledamot/123123/bogus-mp', follow=True)

        self.assertEqual(response.status_code, 404)

    def test_singlemp_contains_right_mp(self):
        response = self.client.get(
            '/ledamot/{0}'.format(self.person.intressent_id), follow=True)

        mp = get_object_or_404(Person, pk=self.person.intressent_id)
        self.assertEqual(response.context['mp'], mp)

class AllMpTest(TestCase):

    def test_allmp_resolves_url_correct(self):
        found = resolve('/ledamot/')

        self.assertEqual(found.func, allmp)

    def test_allmp_has_correct_template(self):
        response = self.client.get('/ledamot/')

        self.assertTemplateUsed(response, 'party-mp.html')

    def test_allmp_has_mps_from_different_parties_2014(self):
        PersonWithCommitment(party='S', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='Mp', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='M', commitments__until=date(2014, 9, 29))
        PersonFactory(party='M')

        response = self.client.get('/ledamot/')

        self.assertEqual(response.context['mps'].count(), 3)

