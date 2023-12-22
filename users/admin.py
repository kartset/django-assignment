from django.contrib import admin

# Register your models here.

from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ("test_id", "name")


admin.site.register(Users, UsersAdmin)