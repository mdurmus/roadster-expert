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