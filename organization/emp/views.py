from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework import filters

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']