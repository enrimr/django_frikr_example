# -*- coding: utf-8 -*-
from django import forms
from models import Photo

class LoginForm(forms.Form):

    user_username = forms.CharField(label="Nombre de usuario")
    user_password = forms.CharField(label="Password", widget=forms.PasswordInput())

# lista de tacos http://goo.gl/G2nCu7
BADWORDS = (u'aparcabicis', u'bocachancla', u'abollao', u'limpiatubos', u'mascachapas', u'diseñata')

class PhotoForm(forms.ModelForm):
    """
    Pinta un formulario de una foto
    """
    class Meta:
        model = Photo
        fields = ['name', 'url', 'description', 'license', 'visibility']

    def clean(self):
        cleaned_data = super(PhotoForm,self).clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise forms.ValidationError(badword + u' no está permitido')

        return cleaned_data