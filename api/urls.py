from django.urls import path

from .views import (ListAssesments, ListCreateEvaluations, ListCreatGoals,
                    ManageEvaluation, SchoolInfo, Teachers, UpdateAssesment,
                    UpdateGoal)

urlpatterns = [
    path("schools/", SchoolInfo.as_view(), name="list_schools"),
    path("teachers/", Teachers.as_view(), name="list_teachers"),
    path("evaluations/", ListCreateEvaluations.as_view(), name="list_evaluations"),
    path("evaluations/<int:pk>", ManageEvaluation.as_view(), name="update_evaluations"),
    path("goals/", ListCreatGoals.as_view(), name="list_goals"),
    path("goals/<int:pk>", UpdateGoal.as_view(), name="update_goals"),
    path("assesments/", ListAssesments.as_view(), name="list_assesments"),
    path("assesments/<int:pk>", UpdateAssesment.as_view(), name="update_assesments"),
]
