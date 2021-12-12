from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import (
    Assesment,
    Assesmentcategories,
    Evaluations,
    Goals,
    Recommendations,
    Schools,
    Subcategories,
)

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    fieldsets = (
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
                    "password",
                )
            },
        ),
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
    readonly_fields = ("last_login", "date_joined")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Assesment)
admin.site.register(Assesmentcategories)
admin.site.register(Evaluations)
admin.site.register(Schools)
admin.site.register(Goals)
admin.site.register(Recommendations)
admin.site.register(Subcategories)
