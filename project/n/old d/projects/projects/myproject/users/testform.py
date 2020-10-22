from django import forms

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class ContactForm(MultipleForm):
    title = forms.CharField(max_length=150)
    message = forms.CharField(max_length=200, widget=forms.TextInput)


class SubscriptionForm(MultipleForm):
    email = forms.EmailField()