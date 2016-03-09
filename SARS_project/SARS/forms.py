from django import forms
from django.contrib.auth.models import User
from SARS.models import Query
from SARS.models import UserProfile

class QueryForm(forms.ModelForm):
    query = forms.CharField(max_length=128, help_text="Enter query:")
    print query

    class Meta:
        model = Query
        fields = ('query',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
