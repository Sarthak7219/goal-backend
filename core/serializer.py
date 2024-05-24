from rest_framework import serializers
from . models import *

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields='__all__'
class Case_studySerializer(serializers.ModelSerializer):
    class Meta:
        model = Case_study
        fields='__all__'
class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields='__all__'
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields='__all__'