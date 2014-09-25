from __future__ import absolute_import

import datetime

from django.contrib.auth.models import User

from riksdagen.models import Person
from riksdagen.models import Voting
from .models import UserProfile
from .models import UserVote
from .models import UserSimilarity
from riksdagsrosten.celery import app

def update_or_create(updated_values):
    instance, created = UserSimilarity.objects.get_or_create(**updated_values)
    if created:
        return created
    else:
        UserSimilarity.objects.update(**updated_values)
        return False

@app.task
def update_user_vote_stats(user_pk):
    """Updates the vote count as well as when user last voted"""
    user = User.objects.get(pk=user_pk)
    vote_count = UserVote.objects.filter(user=user).count()
    # This won't be exactly the time the user last voted
    UserProfile.objects.filter(user__pk=user_pk).update(
        nr_votes=vote_count, last_voted_on=datetime.datetime.now())

@app.task
def similarity_calculate_votes(mp_pk, user_pk):

    """
    alternative way
    # you need order_by as well.
    votes_packet = UserVote.objects.filter(user__pk=user_pk).values('voting_id', 'vote')
    voting_ids = (d['voting_id'] for d in votes)
    user_votes = (d['vote'] for d in votes)
    mp_votes = Voting.objects.filter(fk_voting_person__pk=mp_pk,
                voting_id__in=voting_ids).values_list('vote', flat=True)

    mp_user_vote = zip(user_votes, mp_votes)
    similar_votes = ((user, mp) for user, mp in mp_user_vote if user==mp)
    votesum = sum(1 for x in similar_votes) # length of iterable
    total_votes = sum(1 for vote in user_votes
                if vote == 'Ja' or vote == 'Nej')
    # try block here.
    percentage = votesum/total_votes

    """

    user = User.objects.get(pk=user_pk)
    votes = UserVote.objects.filter(user=user)
    mp = Person.objects.select_related('votes').get(pk=mp_pk)
    d = {}
    vote_sum = 0
    total_votes = 0
    # TODO: This could be made into two chords.
    for v in votes:
        try:
            mp_vote = mp.votes.get(voting_id=v.voting_id).vote
            if mp_vote == v.vote:
                vote_sum += 1
            if mp_vote == 'Ja' or mp_vote == 'Nej':
                total_votes += 1
        except Voting.DoesNotExist:
            print('Skipping this vote!')
    try:
        percentage = (vote_sum/total_votes)*100
    except ZeroDivisionError:
        percentage = 0
    d = {
        'user': user,
        'percentage': percentage,
        'common_votes': total_votes,
        'mp': mp
        }
    update_or_create(d)


@app.task
def similarity_cycle_mps(user_pk):
    user = User.objects.get(pk=user_pk)
    mps = mps = Person.objects.filter(
            commitments__until=datetime.date(2014, 9, 29),
            commitments__role_code__exact='Riksdagsledamot')

    for mp in mps:
        similarity_calculate_votes.delay(mp.pk, user.pk)

