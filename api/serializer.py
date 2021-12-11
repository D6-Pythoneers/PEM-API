from rest_framework import serializers

from accounts.models import CustomUser

from .models import Schools,Assesment,Assesmentcategories,Evaluations


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

# class ManagersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = (
#             "name",
#             "role",
#             "school_id",
#             "nid",
#             "eid",
#             "qualification",
#             "directorate",
#             "last_login",
#         )

# class AssesmentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Assesment
#         fields = ("indicator","first_evaluation","final_evaluation","score")


# class AssesmentcategoriesSerializer(serializers.ModelSerializer):
#       category = AssesmentSerializer(many=True)
#       class Meta:
#         model = Assesmentcategories
#         fields = ("category" ,)
class ManageEvaluationsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Evaluations
        fields = "__all__"

