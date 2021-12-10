from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "role",
                    "school_id",
                    "nid",
                    "eid",
                    "qualification",
                    "directorate",
                    "username",
                    "password1",
                    "password2",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
