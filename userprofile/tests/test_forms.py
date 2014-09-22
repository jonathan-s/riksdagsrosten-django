import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from userprofile.forms import UserProfileForm
from userprofile.models import UserProfile


class UserProfileFormTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(username='joe', password='pass')

    def test_form_renders_field_inputs(self):
        form = UserProfileForm()
        self.fail(form.as_p())

    def test_form_validation(self):
        form = UserProfileForm(instance=self.u.profile, data={
            'open_profile': True,
            'user': self.u.pk
            })
        form.save()
        count = UserProfile.objects.all().count()
        self.assertEqual(count, 1)

    def test_form_doesnt_write_over_votes_or_date(self):
        form = UserProfileForm(instance=self.u.profile, data={
            'open_profile': True,
            'user': self.u.pk
            })
        form.save()
        profile = UserProfile.objects.get(user=self.u)
        self.assertEqual(profile.last_voted_on, None)


