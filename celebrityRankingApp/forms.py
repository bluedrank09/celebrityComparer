from socket import fromshare
from django import forms

class InputCelebrityNames(forms.Form):
    first_celebrity = forms.BooleanField(label="Benedict Cumberbatch", required=False)
    second_celebrity = forms.BooleanField(label="Tom Hiddleston", required=False)
    third_celebrity = forms.BooleanField(label="Scarlett Johansson", required=False)
    fourth_celebrity = forms.BooleanField(label="Elizabeth Olsen", required=False)
    fifth_celebrity = forms.BooleanField(label="Chris Hemsworth", required=False)

