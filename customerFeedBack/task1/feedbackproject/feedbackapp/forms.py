
from django import forms

from.models import CustomerFeedback

class Feedbackform(forms.ModelForm):
    class Meta:
        model=CustomerFeedback

        fields = ['name', 'message', 'rating']

    rating = forms.IntegerField(
        label='Rating',
        widget=
            forms.NumberInput(attrs={
            'type': 'number',
            'min': 1,
            'max': 5,
            'name':forms.FileInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
          
        })
    )
    