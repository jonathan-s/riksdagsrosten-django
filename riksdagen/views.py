from datetime import date

from django.shortcuts import render, redirect, get_object_or_404

from riksdagen.models import Person

"""
Todo
* make an orm manager for MPs for 2014.

"""

# Create your views here.
def party(request):
    pass

def partywithname(request, partyname):
    # add dictionary so {'Socialdemokraterna': 'S'} etc.
    mps = Person.objects.filter(
            party__iexact=partyname, commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})

def singlemp(request, mp_id, nameslug=None):
    mp = get_object_or_404(Person, pk=mp_id)
    correct_slug = "{0}-{1}".format(mp.firstname, mp.lastname)

    if nameslug == None or nameslug != correct_slug:
        return redirect('singlemp', mp_id=mp_id, nameslug=correct_slug, permanent=True)
    else:
        return render(request, 'mp.html', {'mp': mp})

def allmp(request):
    mps = Person.objects.filter(commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})