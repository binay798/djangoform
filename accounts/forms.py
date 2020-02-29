from django import forms


class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))