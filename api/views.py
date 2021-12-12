from rest_framework import generics

from accounts.models import CustomUser

from .models import Schools ,Evaluations, Assesment,Goals
from .serializer import (
    SchoolsSerializer,
    TeachersSerializer,
    ManageEvaluationsSerializer,
    AssesmentSerializer,
    GoalsSerializer,
    )


class SchoolInfo(generics.ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer


class Teachers(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role="teacher")
    serializer_class = TeachersSerializer


class Assesment(generics.ListAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer

class ManageEvaluations(generics.ListCreateAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = ManageEvaluationsSerializer

class Goals(generics.ListCreateAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer
