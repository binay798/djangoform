from django import forms


class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password1 = forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',max_length=30,widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100)