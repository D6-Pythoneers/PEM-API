from rest_framework import serializers

from accounts.models import CustomUser

from .models import Schools


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = (
            "school_id",
            "school_manager",
            "school_name",
            "evaluated",
            "academic_year",
        )
        labels = {"evaluated": "complete"}


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "name",
            "role",
            "school_id",
            "nid",
            "eid",
            "qualification",
            "directorate",
            "last_login",
        )
