from django import forms
from django.conf import settings
from django.contrib import admin
from django.utils import timezone
from datetime import datetime, timedelta, time
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
import datetime
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.core import validators

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username= forms.CharField(widget=forms.TextInput
                              (attrs={'placeholder':'User Name'}),help_text='A user with this Username alredy exist')
    full_name= forms.CharField(widget=forms.TextInput
                              (attrs={'placeholder':'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput
    (attrs={'placeholder': 'Email Address', 'css': 'mycss'}))

    phone_number= forms.IntegerField(widget=forms.NumberInput
                                     (attrs={'placeholder':'Phone Number'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput
                                (attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput
                                (attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = MyUser
        fields = ('username', 'full_name', 'email', 'phone_number',)


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean(self):

        username= self.cleaned_data['username']
        phone_number= self.cleaned_data['phone_number']
        email= self.cleaned_data['email']
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        # if MyUser.objects.filter(username=self.cleaned_data['username']).exists():
        #         raise  ValidationError ('{} Already exist !'.format(username).capitalize())
        #
        #
        # if MyUser.objects.filter(email=self.cleaned_data['email']).exists():
        #     raise  ValidationError ('{} Already exist !'.format(email).capitalize())
        #
        # if password2 != password1:
        #
        #     raise ValidationError('password missmatch !').capitalize()
        #
        # if len(password1) < 8:
        #     raise ValidationError("paswword length too short !").capitalize()
        #

        # if password1[0] != password1[0].upper():
        #     raise ValidationError('Password first letter should be capital letter')



class UserLoginForm(forms.ModelForm):

    email= forms.EmailField(widget=forms.EmailInput
                            (attrs={'placeholder': 'Your Email Adress'}))
    password1 = forms.CharField(widget=forms.PasswordInput
                            (attrs={'placeholder': 'Your Password'}))

    class Meta:
        model = MyUser
        fields = ('email',)


    def clean(self):
        email= self.cleaned_data["email"]

        password1= self.cleaned_data.get('password1')


        if MyUser.objects.filter(email= email).exists():

            pass

        else:

            raise ValidationError('{} does not exist'.format(email)).capitalize()

        if MyUser.objects.filter(password=password1).exists():

            pass

        else:

            raise ValidationError('Please check your Password').capitalize()


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email','phone_number', 'full_name', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserResetPassword(PasswordResetForm):

    email = forms.EmailField(widget=forms.EmailInput
                            (attrs={'placeholder': 'Your Email Adress'}))


    def clean(self):

        email= self.cleaned_data['email']

        print(email)
        user=MyUser.objects.filter(email=email)

        if user.exists():

            pass
        else:


            raise ValidationError('{} Does not Exist '.format(email))

class UserChangePasswordForm(SetPasswordForm):


    new_password1 =  forms.CharField(widget=forms.TextInput
                                    (attrs={'placeholder': 'New password'}))
    new_password2 = forms.CharField(widget=forms.TextInput
                                    (attrs={'placeholder': 'Confirm password'}))


    def clean(self):
        cleaned_data = super().clean()

        pass1= cleaned_data.get('new_password1')
        pass2= cleaned_data.get('new_password2')

        check_letter= pass1[0].upper()


        if len(pass1) < 5:
            raise ValidationError("Paswword length too short")

        if pass2 != pass1:
            raise ValidationError('Password Missmatch')

        if pass1[0] != check_letter:
            raise ValidationError('Password first letter should be capital letter')

        # if '1' or '!' not in pass1:
        #     raise ValidationError('Please use special characters for a stronger Password')

