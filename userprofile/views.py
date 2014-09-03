from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from riksdagen.models import Voting
from .models import UserVote
from .models import UserSimilarity
from .models import UserProfile

@login_required
def userprofile(request):
    votes = UserVote.objects.filter(user__pk=request.user.pk)[:5]
    similarity = UserSimilarity.objects.filter(user__pk=request.user.pk)[:5]

    return render(request, 'userprofile.html', {
        'votes': votes, 'similarity': similarity
        })

def openprofile(request, username):
    """This could probably be mashed together with userprofile"""
    userprofile = get_object_or_404(UserProfile, user__username=username)
    if userprofile.open_profile == False:
        raise Http404

    votes = UserVote.objects.filter(user__username=username)[:5]
    similarity = UserSimilarity.objects.filter(user__username=username)[:5]


    return render(request, 'userprofile.html', {
        'votes': votes,
        'similarity': similarity,
        'userprofile': userprofile
        })

def poll_detail_vote(request, doc_id, doc_item, vote):
    if request.user.is_authenticated():
        vote = Voting.objects.get(document__doc_id=doc_id, doc_item=doc_item)
        update = { data: vote.__dict__.get(data) for data in UserVote.get_field_names()}
        update['user'] = request.user
        update['document'] = vote.document
        update['importance'] = 0 # feature not implemented yet
        UserVote.objects.create(**update)
        return redirect('/votering/{}'.format(doc_id))
    else:
        raise PermissionDenied

def user_settings(request):
    pass

# Create your views here.
