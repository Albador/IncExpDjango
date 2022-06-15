from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from IncExp.models import Booking


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    # clean with case-insensitive usernames
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        User = get_user_model()
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with that username already exists.')
        return cleaned_data

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['description', 'value', 'currency', 'date']
        widgets = {
            'date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}),
        }
