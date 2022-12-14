from django import forms
from wistara.models import Reservation, Review, Subcribe

class SubcribeForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Your email here'}))

    class Meta():
        model = Subcribe
        fields = ('email',)


class ReservationForm(forms.ModelForm):

    class Meta():
        model = Reservation
        fields = ('full_name', 'phone_number', 'table_package', 'table_sit')

class ReviewForm(forms.ModelForm):

    class Meta():
        model = Review
        fields = ('customer_photo', 'customer_name', 'customer_review')