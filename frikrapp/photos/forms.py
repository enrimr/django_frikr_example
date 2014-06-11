from django import forms

class LoginForm(forms.Form):

    user_username = forms.CharField(label="Nombre de usuario")
    user_password = forms.CharField(label="Password", widget=forms.PasswordInput())