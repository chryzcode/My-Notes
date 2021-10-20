from django import forms
from apis.models import Note



class addNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

        widgets={
                'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Note title'}),
                'body':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Start writing...'}),
        }