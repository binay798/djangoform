from django import forms
from .models import Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['topic','desc','img']

        widgets = {
            'topic':forms.TextInput(attrs={'class':'form-control '}),
            'desc':forms.Textarea(attrs={'class':'form-control '}),
            
            
        }




