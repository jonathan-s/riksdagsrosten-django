from django import forms

from .models import UserProfile

class UserProfileForm(forms.models.ModelForm):
    """docstring for UserProfileForm"""
    def __init__(self, arg):
        super(ItemForm, self).__init__()
        self.arg = arg

    def Meta:
        model = UserProfile