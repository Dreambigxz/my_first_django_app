from . models import MyUser
from django import forms
from django.forms import ModelForm


#get all user email

mail = MyUser.objects.values_list('email', flat=True)

for mail in mail:
    pass

Cities = [
    ('Audio', (mail
    ))
]


class SendMailForm(forms.Form):

   message= forms.CharField(widget=forms.Textarea)
   users= forms.ChoiceField(choices=Cities)



