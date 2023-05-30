from django.shortcuts import render
from .serializers import (DepartmentSerializer,PersonelSerializer,DepartmentPersonelSerializer)
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView)
from .models import Department,Personel

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonelListCreateView(ListCreateAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer


class PersonelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer

class DepartmentPersonelView(ListAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentPersonelSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned department to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)