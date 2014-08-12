from datetime import date

from django.shortcuts import render, redirect, get_object_or_404

from riksdagen.models import Person, Voting, Document
from riksdagen.constants import GOVORGAN

"""
Todo
* make an orm manager for MPs for 2014.
* add a dictionary for partywithme

"""

# Create your views here.
def party(request):
    render(request, 'party.html')

def partywithname(request, partyname):
    # add dictionary so {'Socialdemokraterna': 'S'} etc.
    mps = Person.objects.filter(
            party__iexact=partyname, commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})



def singlemp(request, mp_id, nameslug=None):
    mp = get_object_or_404(Person, pk=mp_id)
    correct_slug = "{0}-{1}".format(mp.firstname, mp.lastname)
    # make select_related to save queries.

    if nameslug == None or nameslug != correct_slug:
        return redirect('singlemp', mp_id=mp_id, nameslug=correct_slug, permanent=True)

    vote = Voting.objects.filter(
        fk_voting_person__intressent_id__exact=mp_id) #qs
    absent = vote.filter(vote__exact='Frånvarande').count()
    total_votes = vote.count()
    presence = round((1 - (absent/total_votes)) * 100, 1) # if something is zero?

    d = Document.objects.extra(select={'vote': 'riksdagen_voting.vote', 'person': 'riksdagen_voting.namn'},tables=['riksdagen_voting', 'riksdagen_person'],where=['riksdagen_voting.hangar_id=riksdagen_document.hangar_id',"riksdagen_person.intressent_id=riksdagen_voting.fk_voting_person_id", "riksdagen_person.intressent_id='{0}'".format(mp_id),"riksdagen_voting.doc_item=1"]).distinct('doc_id')[:5]

    return render(request, 'mp.html',
        {'mp': mp, 'absent': absent, 'total_votes': total_votes,
        'presence': presence, 'documents': d})

def allmp(request):
    mps = Person.objects.filter(commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})