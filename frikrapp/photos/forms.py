from django import forms

class LoginForm(forms.Form):

    user_username = forms.CharField()
    user_password = forms.CharField()