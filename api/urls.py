from django.urls import path

from .views import (
    ManageEvaluations,
    SchoolInfo,
    Teachers,
    Assesment,
    Goals,
    )

urlpatterns = [
    path('school_info/', SchoolInfo.as_view(), name='School_info'),
    path('teachers/', Teachers.as_view(), name='Teachers'),
    path('manage-evaluations/', ManageEvaluations.as_view(), name='mange_evaluations'),
    path('assesments/', Assesment.as_view(), name='assesments'),
    path('goals/', Goals.as_view(), name='goals'),]
