from django.forms import ModelForm
from django import forms
from .models import Reservation


class ReservationForm(ModelForm):

    expected_date= forms.DateField(widget=forms.DateInput
        (attrs={'placeholder': 'Expected Date',
         'css': 'mycss',
        'data-select':'datepicker'}), input_formats=['%d/%m/%Y'],)

    expected_time=forms.TimeField(widget=forms.TimeInput(
        attrs={'placeholder':'Expected Time',
               'css': 'mycss',
               'id':'reservation_time'}), input_formats=['%H:%M'], required=False
    )

    total_person= forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Total Persons'}
    ))

    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'short message (optionam)'}
    ))

    def clean(self):

        expected_date= self.cleaned_data.get('expected_date')



    class Meta():
        model= Reservation
        fields= ('expected_date', 'expected_time', 'total_person', 'message',)