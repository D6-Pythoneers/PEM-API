from django.urls import path

from .views import SchoolInfo,Teachers,Managers

urlpatterns = [
    path('school_info/', SchoolInfo.as_view(), name='School_info'),
    path('teachers/', Teachers.as_view(), name='Teachers'),
    path('managers/', Managers.as_view(), name='Managers'),
]
