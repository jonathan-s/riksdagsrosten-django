from django import forms

from .models import UserProfile

CHOICES = (
    (False, 'Nej'),
    (True, 'Ja'),
)

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('open_profile', 'user')
        widgets = {
            'open_profile': forms.fields.Select(choices=CHOICES),
            'user': forms.fields.HiddenInput()
        }
        labels = {
            'open_profile': 'Öppen profil',
        }