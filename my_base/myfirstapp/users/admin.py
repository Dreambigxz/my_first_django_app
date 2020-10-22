from django.contrib import admin
from .models import MyUser, Testing
from .forms import  UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
# Register your models here.



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'expired', 'has_got_mail', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('full_name','tokken', 'date_of_birth', 'expired', 'has_got_mail', 'phone_number',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name',
                       'username',
                       'email',
                       'phone_number',
                       'date_of_birth',
                        'password1',
                       'password2'),
        }),
    )


    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)


class CustomUserAdmin(admin.ModelAdmin):

    #add_form = CustomUserCreationForm
    # form = TestForm
    # model = Testing

    fields = ['name', 'age']
    list_display = ['name', 'age']


admin.site.register(Testing, CustomUserAdmin)
