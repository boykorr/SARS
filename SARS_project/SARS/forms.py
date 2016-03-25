from django import forms
from django.contrib.auth.models import User
from SARS.models import Query, UserProfile, Review
from django.forms import ModelForm, Textarea


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Title: ") #forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'8', 'cols':'24'}), max_length=500, help_text="Description: ") #widget=forms.Textarea
    pool_size = forms.IntegerField(widget=forms.HiddenInput()) #forms.NumberInput()
    abstracts_judged = forms.IntegerField(widget=forms.HiddenInput()) #forms.NumberInput()
    documents_judged = forms.IntegerField(widget=forms.HiddenInput()) #forms.NumberInput()

    class Meta:
        model = Review
        field = ('title', 'description',)
        exclude = ('user', 'date_started', 'pool_size', 'abstracts_judged', 'documents_judged',)


class QueryForm(forms.ModelForm):
    queryBox = forms.CharField(widget=forms.TextInput(attrs={"size":"120"}))

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
