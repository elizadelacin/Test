from django import forms
from .models import Comment_form, Contact_form
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment_form
        fields = ['name', 'email', 'website', 'message']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_form
        fields = ['name', 'email', 'subject', 'message']


class UserCreation(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-4'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control p-4'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password_confirm != password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

