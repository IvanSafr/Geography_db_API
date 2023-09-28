from rest_framework import viewsets

from .serializers import SudentSerializer
from .models import student_info

class StudentViewSet(viewsets.ModelViewSet):
    queryset = student_info.objects.all().order_by('id')
    serializer_class = SudentSerializer