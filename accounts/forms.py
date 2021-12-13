from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "role",
            "school_id",
            "username",
            "nid",
            "eid",
            "qualification",
            "directorate",

        )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "role",
            "school_id",
            "username",
            "nid",
            "eid",
            "qualification",
            "directorate",

        )
