from django.urls import path

from .views import SchoolInfo,Teachers

urlpatterns = [
    path('school_info/', SchoolInfo.as_view(), name='School_info'),
    path('teachers/', Teachers.as_view(), name='Teachers')
]
