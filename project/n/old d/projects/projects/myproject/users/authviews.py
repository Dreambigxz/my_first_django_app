from django.shortcuts import (render, HttpResponse,
                              get_object_or_404, redirect, resolve_url,
                              reverse,)

from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.utils.http import (
    url_has_allowed_host_and_scheme, urlsafe_base64_decode,)
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


from .forms import UserCreationForm, UserLoginForm, UserResetPassword
from django.core.exceptions import ValidationError

from django.conf import settings
from .models import MyUser


# Create your views here.

###########Reset password###########
class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            **(self.extra_context or {})
        })
        return context


class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'users/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'users/password_reset_form.html'
    title = ('Password reset')
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'



