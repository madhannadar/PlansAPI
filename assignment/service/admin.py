from django.contrib import admin
from .models import Plans,CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    list_display = ('email',)
    # search_fields = ('email',)
    ordering = ('email',)
    # fieldsets =(
    #     (None, {'fields': ('name','venue', 'event_date', 'description', 'manager')}),
    # )
    # fields = ('name','email','password','salutation')
    fieldsets = (
         ('Required Information', {
             'description': "These fields are required for each event.",
             'fields': (('name','email'), 'salutation','password')
         }),
     )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )

    # fieldsets =  CustomUser._meta.get_all_field_names()

# admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
# admin
admin.site.register(Plans)
# admin.site.unregister(User)
# admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(CustomUser)
