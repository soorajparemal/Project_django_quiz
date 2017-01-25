
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    school=forms.CharField(max_length=100)
    standard=forms.IntegerField()

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email' ,'password')
    Working_at  = forms.CharField(max_length=100)
    Teaching_standard = forms.IntegerField()

