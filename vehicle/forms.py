from .models import Comment, Profile
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for post comments
    """

    class Meta:
        model = Comment
        fields = ('comment',)


class UserUpdateForm(forms.ModelForm):
    """
    Form for User update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for Profile update
    """

    class Meta:
        model = Profile
        fields = ['image', ]
