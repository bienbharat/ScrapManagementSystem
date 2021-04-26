from django.contrib.auth.admin import UserAdmin
from userPlus.forms import *
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.conf.urls import url
from django.contrib import admin
from userPlus import models
from django.contrib import messages
from django.contrib.admin import ModelAdmin
from userPlus import signals

sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


class BaseUserAdmin(UserAdmin):
    form = UserChagneForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = None
    list_display = ('EmailId', 'Name', 'Mobile', 'IsActive', 'is_staff',
                    'IsVerified', 'last_login',)

    """
    Set fieldsets to control the layout of admin “add” and “change” pages.
    """
    fieldsets = (
        (None, {
            'fields': ('EmailId', 'password', 'Mobile')
        }),
        ('Security', {
            'fields': (
                'IsActive', 'is_superuser', 'is_staff', 'LastLoginIP', 'groups', 'user_permissions',),
        }),
        ('Important dates', {
            'fields': ('last_login', 'CreatedOn', 'UpdatedOn',),
        }),
    )

    """
    The add_fieldsets class variable is used to define the fields that will be displayed on the create user page.
    """
    add_fieldsets = (
        (None, {
            'fields': ('EmailId', 'Name'),
        }),
        ('Preferences', {
            'fields': 'IsActive',
        }),
        ('Security', {
            'fields': ('is_superuser', 'is_staff', 'groups', 'user_permissions',),
        }),
    )
    search_fields = ('EmailId', 'Name')
    ordering = ('EmailId',)
    readonly_fields = ('last_login', 'CreatedOn', 'UpdatedOn',)
    actions = ('reset_passwords',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('IsActive', 'IsVerified')

    def queryset(self, request):
        queryset = super(BaseUserAdmin, self).queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)
        return queryset

    def get_urls(self):
        return [url(r'^(/d+)/change/password/$',
                    self.admin_site.admin_view(self.user_change_password))
                ] + super(BaseUserAdmin, self).get_urls()

    # def get_readonly_fields(self, request, obj=None):
    #     readonly_fields = super(BaseUserAdmin, self).get_readonly_fields(request, obj)
    #     if not request.user.is_superuser:
    #         readonly_fields = list(readonly_fields)
    #         readonly_fields.append('is_superuser')
    #         readonly_fields = set(readonly_fields)
    #     return readonly_fields

    """ 
    figure out where to redirect after the 'save' button has been pressed
    when adding a new object.
    """

    def response_post_save_add(self, request, obj):
        response = super(BaseUserAdmin, self).response_post_save_add(request, obj)
        # change the password to a random password
        pw = obj.set_random_password()
        print('User {}\'s new random password: {}'.format(obj.EmailId, pw))
        self.message_user(request, 'User {}\'s new random password: {}'.format(obj.EmailId, pw), messages.SUCCESS)
        return response


# Register your models here.
admin.site.register(models.User, BaseUserAdmin)
