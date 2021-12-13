from rest_framework import generics

from accounts.models import CustomUser

from .models import Assesment, Evaluations, Goals, Schools
from .serializer import (
    AssesmentSerializer,
    GoalsSerializer,
    ManageEvaluationsSerializer,
    SchoolsSerializer,
    TeachersSerializer,
)


class SchoolInfo(generics.ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer


class Teachers(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role="teacher")
    serializer_class = TeachersSerializer


class ListCreateEvaluations(generics.ListCreateAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = ManageEvaluationsSerializer


class ManageEvaluation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluations.objects.all()
    serializer_class = ManageEvaluationsSerializer


class ListCreatGoals(generics.ListCreateAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer


class UpdateGoal(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer


class ListAssesments(generics.ListCreateAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer


class UpdateAssesment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assesment.objects.all()
    serializer_class = AssesmentSerializer
