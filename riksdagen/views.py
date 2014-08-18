from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from riksdagen.models import Person, Voting, Document, VotingDistinct
from riksdagen.constants import GOVORGAN, PARTY_NAME, PARTY

def home(request):
    return render(request, 'home.html')

def polls(request, category=None):
    # do a subquery with distinct through extra. It should work, this is still a rather slow query
    # http://stackoverflow.com/questions/9795660/postgresql-distinct-on-without-ordering
    d = VotingDistinct.objects.select_related('document').filter(doc_item__exact=1, pertaining__exact='sakfrågan').order_by('-date')

    if category and GOVORGAN.get(category):
        d = d.filter(govorgan__exact=category)[:20]
    elif category:
        return redirect('polls', permanent=True)
    else:
        d = d[:20]

    return render(request, 'polls.html', {'documents': d, 'govorgan': GOVORGAN })

def party(request):
    counts = {}
    # this is somewhat expensive, find a way to cache this.
    for party in PARTY_NAME.keys():
        print(party)
        counts['{0}'.format(party)] = Person.objects.filter(
            party__exact=PARTY_NAME[party], commitments__until=date(2014, 9, 29), commitments__role_code__exact='Riksdagsledamot').count()

    return render(request, 'party.html', {'counts': counts, 'party_name': PARTY_NAME })

def partywithname(request, partyname):
    if PARTY_NAME.get(partyname):
        mps = Person.objects.filter(
            party__exact=PARTY_NAME[partyname], commitments__until=date(2014, 9, 29),
            commitments__role_code__exact='Riksdagsledamot')
    else:
        raise Http404

    return render(request, 'party-mp.html', {'mps': mps})



def singlemp(request, mp_id, nameslug=None):
    mp = get_object_or_404(Person, pk=mp_id)
    correct_slug = "{0}-{1}".format(mp.firstname, mp.lastname).replace(' ', '-')
    # make select_related to save queries.

    if nameslug == None or nameslug != correct_slug:
        return redirect('singlemp', mp_id=mp_id, nameslug=correct_slug, permanent=True)

    vote = Voting.objects.filter(
        fk_voting_person__intressent_id__exact=mp_id) #qs
    absent = vote.filter(vote__exact='Frånvarande').count()
    total_votes = vote.count()
    if total_votes != 0:
        presence = round((1 - (absent/total_votes)) * 100, 1)
    else:
        presence = 0

    d = Document.objects.extra(select={'vote': 'riksdagen_voting.vote', 'person': 'riksdagen_voting.namn'},tables=['riksdagen_voting', 'riksdagen_person'],where=['riksdagen_voting.hangar_id=riksdagen_document.hangar_id',"riksdagen_person.intressent_id=riksdagen_voting.fk_voting_person_id", "riksdagen_person.intressent_id='{0}'".format(mp_id),"riksdagen_voting.doc_item=1"]).distinct('doc_id')[:5]

    return render(request, 'mp.html',
        {'mp': mp, 'absent': absent, 'total_votes': total_votes,
        'presence': presence, 'documents': d})

def allmp(request):
    mps = Person.objects.filter(commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})