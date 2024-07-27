from rest_framework import serializers
from .models import *

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'

class ImageCaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Case_Study
        fields = '__all__'

class ImageWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Workshop
        fields = '__all__'

class CaseStudyThemeDescriptionSerializer(serializers.ModelSerializer):
    theme_title = serializers.CharField(source='theme.title', read_only=True)

    class Meta:
        model = CaseStudyThemeDescription
        fields = '__all__'

class CaseStudySerializer(serializers.ModelSerializer):
    case_study_themes = CaseStudyThemeDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Case_study
        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
