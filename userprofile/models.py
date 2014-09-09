import datetime

from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

from riksdagen.models import VotingBase
from riksdagen.models import Person
from riksdagen.models import Document


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    last_voted_on = models.DateTimeField(null=True)
    open_profile = models.BooleanField(default=False)
    nr_votes = models.IntegerField(default=0)

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

    class Meta:
        unique_together = ('user', 'voting_id')

    def __str__(self):
        return "{0}:{1} Röst: {2}".format(
            self.party_year, self.label, self.vote)

class UserSimilarity(models.Model):
    """This is implicitly a many-to-many model but with data in between"""
    user = models.ForeignKey(User, related_name='similarity')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    common_votes = models.IntegerField()
    mp = models.ForeignKey(Person, related_name='user_similarity')

    def __str__(self):
        return "{0} vs {1}: {2}%".format(
            self.user, self.mp, self.percentage)
