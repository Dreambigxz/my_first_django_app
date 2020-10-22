from functools import wraps
from django.shortcuts import redirect

def redirect_auth_users(view_func):
    def wrapped(request, *args, **kwargs):
        if request.user.is_authenticated:
            # path = request.build_absolute_uri()
            # from django.contrib.auth.views import redirect_to_login
            return redirect('account')
        else:
            try:
                # profile = request.user.profile
                pass
            except :
                pass
            else:
                return view_func(request, *args, **kwargs)
    return wrapped
