# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['pk', 'username',]

    add_fieldsets = UserAdmin.fieldsets + (
        (None,{
            'fields':('roles',)
        }),
 #        (None, {
 #            'classes': ('wide',),
 #            'fields': ('username','email', 'first_name', 'last_name', 'roles', 'password1', 'password2')}
 #        ),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None,{
            'fields':('roles',)
        }),
#        ('Add content',{
#            'fields':('username', 'first_name', 'last_name', 'roles', 'password1', 'password2')
#        })
    )

    '''
    update_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'roles', 'password1', 'password2')}
        ),
    )
    '''

admin.site.register(CustomUser, CustomUserAdmin)