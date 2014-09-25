from django.db.models import F
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from riksdagen.models import Voting
from riksdagen.models import VotingAgg
from .models import UserVote
from .models import UserSimilarity
from .models import UserProfile
from .forms import UserProfileForm
from userprofile.tasks import similarity_cycle_mps
from userprofile.tasks import update_user_vote_stats

@login_required
def userprofile(request):
    user = User.objects.select_related(
        'votes', 'socialaccount_set', 'profile', 'similarity').get(pk=request.user.pk)
    votes = user.votes.all()[:5]
    similarity = user.similarity.all()[:5]
    fb_id = user.socialaccount_set.get().uid

    return render(request, 'userprofile.html', {
        'votes': votes,
        'similarity': similarity,
        'user': user,
        'fb_id': fb_id
        })

def openprofile(request, username):
    """This could probably be mashed together with userprofile"""
    user = get_object_or_404(
        User.objects.select_related(
            'votes', 'socialaccount_set', 'profile', 'similarity'),
        username=username)
    if user.profile.open_profile == False:
        raise Http404

    votes = user.votes.all()[:5]
    similarity = user.similarity.all()[:5]
    fb_id = user.socialaccount_set.get().uid

    return render(request, 'userprofile.html', {
        'votes': votes,
        'similarity': similarity,
        'user': user,
        'fb_id': fb_id
        })

def add_vote_votingagg(vote, voting_id, oldobj=None):
    mapping = {'Ja': 'u_q1_yes', 'Nej': 'u_q1_no'}
    if oldobj:
        updatedict = {mapping[oldobj.vote]:F(mapping[oldobj.vote]) - 1}
        VotingAgg.objects.filter(voting_id=voting_id).update(**updatedict
            )

    if vote == 'Ja':
        VotingAgg.objects.filter(voting_id=voting_id).update(
            u_q1_yes=F('u_q1_yes') + 1)
    elif vote == 'Nej':
        VotingAgg.objects.filter(voting_id=voting_id).update(
            u_q1_no=F('u_q1_no') + 1)
    else:
        pass


def update_or_create(model, filterdic, defaults):
    """Returns 'oldobj', newobj and if it is created"""
    # user ** to expand dictionary
    #defaults.update(filterdic)
    obj, created = model.objects.get_or_create(defaults=defaults, **filterdic)
    if created:
        return obj, obj, True
    else:
        newobj = model.objects.filter(**filterdic).update(**defaults)
        return obj, newobj, False

def poll_detail_vote(request, doc_id, doc_item, uservote):
    # TODO: change this into a form.
    # Sanitize input
    vote = Voting.objects.filter(
            document__doc_id=doc_id, doc_item=doc_item).first()

    if (uservote != 'Nej' and uservote != 'Ja') or not vote:
        return redirect('/votering/{}'.format(doc_id))

    if request.user.is_authenticated():

        update = { data: vote.__dict__.get(data)
                for data in UserVote.get_field_names() if data not in ['id', 'date_voted']}

        update['user'] = request.user
        update['document'] = vote.document
        update['importance'] = 0 # feature not implemented yet
        update['vote'] = uservote
        oldobj, newobj, created = update_or_create(UserVote,
            {'voting_id': update['voting_id'],
            'user': update['user']}, update)

        if created:
            add_vote_votingagg(uservote, vote.voting_id)
        else:
            add_vote_votingagg(uservote, vote.voting_id, oldobj)
        # tasks
        similarity_cycle_mps.delay(request.user.pk)
        update_user_vote_stats.delay(request.user.pk)
        return redirect('/votering/{}'.format(doc_id))
    else:
        raise PermissionDenied

def user_settings(request):
    user = User.objects.select_related(
        'votes', 'socialaccount_set', 'profile', 'similarity').get(pk=request.user.pk)
    fb_id = user.socialaccount_set.get().uid

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user.profile)

        if form.is_valid():
            print('success')
            print(user.profile.open_profile)
            form.save(commit=True)
            print(user.profile.open_profile)
            return redirect('usersettings')
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=user.profile)
    return render(request, 'settings.html', {
        'user': user,
        'form': form,
        'fb_id': fb_id})


def user_logout(request):
    logout(request)
    return redirect('/')