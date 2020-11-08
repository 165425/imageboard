from django import forms


# Create your views here
class SubmitPostForm(forms.Form):
    name = forms.CharField(label='Naam', max_length=100, required=False)
    text = forms.CharField(label='Tekst', max_length=1000, required=False)
    image = forms.ImageField(label='Afbeelding', required=False)

