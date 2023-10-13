from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.


User = get_user_model()

#admin.site.register(User)

@admin.register(User)   
class User(UserAdmin):
    list_display = ("username", "email","type","first_name", "last_name", "is_staff",)
    fieldsets = (
        (None, {"fields": ("username", "password","type",)}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )