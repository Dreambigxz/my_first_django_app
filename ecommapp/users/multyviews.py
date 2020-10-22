from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from .testform import ContactForm, SubscriptionForm
from .forms import UserCreationForm, UserLoginForm
from users.multiformsinheritance import  *

# def form_redir(request):
#     return render(request, 'pages/form_redirect.html')
#
#
# def multiple_forms(request):
#     if request.method == 'POST':
#         contact_form = ContactForm(request.POST)
#         subscription_form = SubscriptionForm(request.POST)
#         if contact_form.is_valid() or subscription_form.is_valid():
#             # Do the needful
#             return HttpResponseRedirect(reverse('form-redirect'))
#     else:
#         contact_form = ContactForm()
#         subscription_form = SubscriptionForm()
#
#     return render(request, 'pages/multiple_forms.html', {
#         'contact_form': contact_form,
#         'subscription_form': subscription_form,
#     })


class MultipleFormsDemoView(MultiFormsView):
    template_name = "users/testuser.html"
    form_classes = {'contact': ContactForm,
                    'subscription': SubscriptionForm,
                    }

    success_urls = {
        'contact': reverse_lazy('t'),
        'subscription': reverse_lazy('t'),
    }

    def contact_form_valid(self, form):
        title = form.cleaned_data.get('title')
        form_name = form.cleaned_data.get('action')
        print(title)
        return HttpResponseRedirect(self.get_success_url(form_name))

    def subscription_form_valid(self, form):
        email = form.cleaned_data.get('email')
        form_name = form.cleaned_data.get('action')
        print(email)
        return HttpResponseRedirect(self.get_success_url(form_name))


class MultipleFormsAuth(MultiFormsView):
    template_name = "users/login-register.html"
    form_classes = {'login': UserLoginForm,
                    'register': UserCreationForm,
                    }

    success_urls = {
        'contact': reverse_lazy('home'),
        'subscription': reverse_lazy('home'),
    }


    def user_login_form_valid(self, form):

        title = form.cleaned_data.get('username')
        form_name = form.cleaned_data.get('action')
        print(title)

        return HttpResponseRedirect(self.get_success_url(form_name))

    def user_registration_form_valid(self, form):

        email = form.cleaned_data.get('email')
        form_name = form.cleaned_data.get('action')
        print(email)
        return HttpResponseRedirect(self.get_success_url(form_name))