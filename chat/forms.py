from attr import fields
from django import forms
from .models import Account



class AuthForm(forms.ModelForm):
    username = forms.CharField(   max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder' : 'Username'
                
            }
        ),
        label = 'Username',
        required=True
    )
    password = forms.CharField( max_length=30, min_length=6,label='Password', widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': 'form-control',}))


    class Meta:
        model = Account
        fields = ['username','password']