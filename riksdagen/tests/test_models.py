from django.test import TestCase

from riksdagen.models import VotingAgg
from .factories import DocumentFactory
from .factories import VotingFactory

class VotingAggTest(TestCase):

    def setUp(self):
        self.d = DocumentFactory()
        VotingFactory.create_batch(50, document=self.d)

    def test_votingagg_gets_created(self):
        count = VotingAgg.objects.all().count()
        self.assertEqual(count, 0) # no aggregates before document saved

        self.d.save()
        agg = VotingAgg.objects.all()
        self.assertEqual(agg.count(), 1)

