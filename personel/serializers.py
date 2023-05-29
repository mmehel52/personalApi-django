from rest_framework import serializers
from .models import Department,Personel

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields='__all__'

class PersonelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Personel
        fields='__all__'