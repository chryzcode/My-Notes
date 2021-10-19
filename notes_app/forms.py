from django import forms
from apis.models import Note



class addNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

        widgets={
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'body':forms.Textarea(attrs={'class':'form-control'}),
        }