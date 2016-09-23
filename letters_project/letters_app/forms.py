from django import forms


class LetterForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=200)
    text = forms.CharField(label='Tekst', widget=forms.Textarea)
    author = forms.CharField(label='Autor', max_length=200)
