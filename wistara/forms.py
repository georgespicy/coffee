from django import forms
from wistara.models import Subcribe


class SubcribeForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Your email here'}))

    class Meta():
        model = Subcribe
        fields = ('email',)