from django.contrib import admin
from App.models import Role, Map_Role_User, Address, Social


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'Id',
        'User_Role',
        'CreatedOn',
        'UpdatedOn'
    )


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'User',
        'isPermanent',
        'locality',
        'address',
        'city',
        'state',
        'country',
        'CreatedOn',
        'UpdatedOn'
    )


class MapAdmin(admin.ModelAdmin):
    list_display = (
        'Id',
        'User',
        'Role',
        'CreatedOn',
        'UpdatedOn'
    )


admin.site.register(Role, RoleAdmin)
admin.site.register(Map_Role_User, MapAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Social)
