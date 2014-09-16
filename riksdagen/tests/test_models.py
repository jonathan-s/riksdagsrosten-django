from django.test import TestCase

from riksdagen.models import VotingAgg
from .factories import DocumentFactory
from .factories import VotingFactory

class VotingAggTest(TestCase):

    def setUp(self):
        self.d = DocumentFactory()
        VotingFactory.create_batch(50, document=self.d, vote='Ja')
        VotingFactory.create_batch(25, document=self.d, vote='Nej')

    def test_votingagg_gets_created(self):
        count = VotingAgg.objects.all().count()
        self.assertEqual(count, 0) # no aggregates before document saved

        self.d.save()
        agg = VotingAgg.objects.all()
        self.assertEqual(agg.count(), 1)

    def test_votingagg_contains_right_amount_aggregate(self):
        self.d.save()
        agg = VotingAgg.objects.all().first()

        self.assertEqual(agg.q1_yes, 50)
        self.assertEqual(agg.q1_no, 25)

class DocumentTest(TestCase):

    def test_document_saves_a_html_summary(self):
        do = DocumentFactory(html="""<html><body>
            <a href=""></a><p></p><p></p><p></p>
            <a href=""></a><p></p><p></p><p></p>
            <a href=""></a><p></p><p></p><p></p></body></html>""")
        ptags = """<p></p><p></p><p></p>
            <a href=""></a><p></p><p></p><p></p>
            <a href=""></a>"""
        self.assertEqual(do.summary, ptags)
