from django.db.models import F
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from riksdagen.models import Voting
from riksdagen.models import VotingAgg
from .models import UserVote
from .models import UserSimilarity
from .models import UserProfile
from userprofile.tasks import similarity_cycle_mps
from userprofile.tasks import update_user_vote_stats

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

def add_vote_votingagg(vote, voting_id):
    if vote == 'Ja':
        VotingAgg.objects.filter(voting_id=voting_id).update(
            u_q1_yes=F('u_q1_yes') + 1)
    else:
        VotingAgg.objects.filter(voting_id=voting_id).update(
            u_q1_no=F('u_q1_no') + 1)

def poll_detail_vote(request, doc_id, doc_item, vote):
    # TODO: change this into a form.
    if request.user.is_authenticated():
        vote = Voting.objects.filter(
            document__doc_id=doc_id, doc_item=doc_item).first()

        update = { data: vote.__dict__.get(data)
                for data in UserVote.get_field_names() if data!='id'}
        update['user'] = request.user
        update['document'] = vote.document
        update['importance'] = 0 # feature not implemented yet
        UserVote.objects.get_or_create(
            voting_id=update['voting_id'],
            user=update['user'], defaults=update)

        add_vote_votingagg(vote.vote, vote.voting_id)
        # tasks
        similarity_cycle_mps.delay(request.user.pk)
        update_user_vote_stats.delay(request.user.pk)
        return redirect('/votering/{}'.format(doc_id))
    else:
        raise PermissionDenied

def user_settings(request):
    pass


def user_logout(request):
    logout(request)
    return redirect('/')