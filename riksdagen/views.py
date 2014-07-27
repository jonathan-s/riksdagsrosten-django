from datetime import date

from django.shortcuts import render

from riksdagen.models import Person

# Create your views here.
def party(request):
    pass

def partywithname(request, partyname):
    # add dictionary so {'Socialdemokraterna': 'S'} etc.

    mps = Person.objects.filter(
            party__iexact=partyname, commitments__until=date(2014, 9, 29),
            commitments__role_code__iexact='Riksdagsledamot')

    return render(request, 'party-mp.html', {'mps': mps})