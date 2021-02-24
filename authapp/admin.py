from django.contrib import admin
from authapp.models import User


class UserAdmin(admin.ModelAdmin):
    field = [field.name for field in User._meta.get_fields()]


admin.site.register(User, UserAdmin)
