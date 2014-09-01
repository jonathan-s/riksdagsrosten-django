from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required


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

def user_settings(request):
    pass

# Create your views here.
