from rest_framework import generics

from accounts.models import CustomUser

from .models import Schools ,Evaluations
from .serializer import (
    SchoolsSerializer,
    TeachersSerializer,
    ManageEvaluationsSerializer,
    )


class SchoolInfo(generics.ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer


class Teachers(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role="teacher")
    serializer_class = TeachersSerializer


# class Assesment(generics.ListAPIView):
#     queryset = CustomUser.objects.filter(role="manager")
#     serializer_class = AssesmentcategoriesSerializer

class ManageEvaluations(generics.ListCreateAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = ManageEvaluationsSerializer



