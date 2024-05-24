from rest_framework import serializers
from . models import *

class Case_studySerializer(serializer.ModelSerializer):
    class Meta:
        model = Case_study
        fields='__all__'