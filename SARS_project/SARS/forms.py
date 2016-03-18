from django import forms
from django.contrib.auth.models import User
from SARS.models import Query
from SARS.models import UserProfile
from django.forms import ModelForm, Textarea
#from django.contrib.postgres.forms import SimpleArrayField

class QueryForm(forms.ModelForm):
    queryBox = forms.CharField(max_length=128, help_text="Enter query:")
    #query = ArrayField(forms.CharField(max_length=20))
    #print query

    class Meta:
        model = Query
        fields = ('queryBox',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)