from rest_framework import generics

from accounts.models import CustomUser

from .models import Schools
from .serializer import SchoolsSerializer, TeachersSerializer


class SchoolInfo(generics.ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer


class Teachers(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role="teacher")
    serializer_class = TeachersSerializer
