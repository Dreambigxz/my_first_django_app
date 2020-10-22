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


# class persist_session_vars(object):
#     """
#     Some views, such as login and logout, will reset all session state.
#     (via a call to ``request.session.cycle_key()`` or ``session.flush()``).
#     That is a security measure to mitigate session fixation vulnerabilities.
#
#     By applying this decorator, some values are retained.
#     Be very aware what find of variables you want to persist.
#     """
#
#     def __init__(self, vars):
#         self.vars = vars
#
#     def __call__(self, view_func):
#
#         @wraps(view_func)
#         def inner(request, *args, **kwargs):
#             # Backup first
#             session_backup = {}
#             for var in self.vars:
#                 # try:
#                 session_backup[var] = request.session['device_id']
#                 # except KeyError:
#                 #     pass
#
#             # Call the original view
#             response = view_func(request, *args, **kwargs)
#
#             # Restore variables in the new session
#             for var, value in session_backup.items():
#                 request.session['device_id'] = value
#
#             return response
#
#         return inner


class persist_session_vars(object):
    """ Some views, such as login and logout, will reset all session state.
    However, we occasionally want to persist some of those session variables.
    """

    session_backup = {}

    def __init__(self, vars):
        self.vars = vars

    def __enter__(self):
        for var in self.vars:
            self.session_backup[var] = self.request.session.get('device_id')

    def __exit__(self, exc_type, exc_value, traceback):
        for var in self.vars:
            self.request.session['device_id'] = self.session_backup.get(var)

    def __call__(self, test_func, *args, **kwargs):

        @wraps(test_func)
        def inner(*args, **kwargs):
            if not args:
                raise Exception('Must decorate a view, ie a function taking request as the first parameter')
            self.request = args[0]
            with self:
                return test_func(*args, **kwargs)

        return inner

