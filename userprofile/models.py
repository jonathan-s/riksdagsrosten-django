import datetime

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.models import EmailAddress

from riksdagen.models import VotingBase
from riksdagen.models import Voting
from riksdagen.models import Person
from riksdagen.models import Document

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    last_voted_on = models.DateTimeField()
    open_profile = models.BooleanField()
    nr_votes = models.IntegerField()

    def __str__(self):
        return "{0}'s profile".format(self.user.username)

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class UserVote(VotingBase):
    # is it better to tie uservotes to the user or the userprofile?
    user = models.ForeignKey(User, related_name='votes')
    document = models.ForeignKey(Document, related_name='userdoc_votes')
    importance = models.IntegerField(default=0)
    date_voted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}:{1} Röst: {2}".format(
            self.party_year, self.label, self.vote)

class UserSimilarity(models.Model):
    """This is implicitly a many-to-many model but with data in between"""
    user = models.ForeignKey(User, related_name='similarity')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    common_votes = models.IntegerField()
    mp = models.ForeignKey(Person, related_name='user_similarity')

def update_or_create(updated_values):
    instance, created = UserSimilarity.objects.get_or_create(**updated_values)
    if created:
        return created
    else:
        UserSimilarity.objects.update(**updated_values)
        return False

@receiver(post_save, sender=UserVote)
def update_person(sender, instance, created, raw, using, update_fields, **kwargs):
    count = UserVote.objects.filter(user=instance.user).count()
    UserProfile.objects.filter(user__id=instance.user.id).update(
        nr_votes=count, last_voted_on=datetime.datetime.now())

    mps = Person.objects.filter(
            commitments__until=datetime.date(2014, 9, 29),
            commitments__role_code__exact='Riksdagsledamot')
    votes = UserVote.objects.filter(user=instance.user)

    for mp in mps:
        d = {}
        total_votes = 0
        # getting all similar votes.
        vote_sum = 0
        for v in votes:
            try:
                mp_vote = mp.votes.get(voting_id=v.voting_id).vote
                if mp_vote == v.vote:
                    vote_sum += 1
                if mp_vote == 'Ja' or mp_vote == 'Nej':
                    total_votes += 1
            except Voting.DoesNotExist:
                print('Warning!')
                pass # skip this vote

        d = {
            'user': instance.user,
            'percentage': (vote_sum/total_votes)*100,
            'common_votes': total_votes,
            'mp': mp
            }
        update_or_create(d)


