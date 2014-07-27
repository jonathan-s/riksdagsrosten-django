from datetime import date

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string


from .factories import PersonFactory, PersonWithCommitment
from riksdagen.views import party, partywithname
from riksdagen.models import Person


class PartyTest(TestCase):

    def test_party_resolves_url_correct(self):
        pass

    def test_name_here(self):
        pass

class PartyNameTest(TestCase):

    def test_partyname_resolves_url_correct(self):
        found = resolve('/parti/M/')

        self.assertEqual(found.func, partywithname)
        self.assertEqual(found.kwargs, {'partyname': 'M'})

    def test_partyname_correct_template(self):
        response = self.client.get('/parti/M/')

        self.assertTemplateUsed(response, 'party-mp.html')

    def test_partyname_has_correct_mps(self):
        PersonWithCommitment(party='M', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='S', commitments__until=date(2014, 9, 29))
        PersonWithCommitment(party='M', commitments__until=date(2014, 1, 1))
        #Above should not be in list.
        response = self.client.get('/parti/M/')

        mps = Person.objects.filter(
            party__iexact='M', commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

        self.assertEqual(list(response.context[-1]['mps']), list(mps))

    def test_party_returns_response(self):
        response = self.client.get('/parti/M/')

        self.assertEqual(response.status_code, 200)
