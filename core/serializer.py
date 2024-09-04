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

class Image_Workshop_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image_Workshop
        fields = '__all__'


class Stories_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Stories
        fields = '__all__'



class CollaboratingInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratingInstitute
        fields = ['name', 'logo']  # Include fields you want to serialize


class Homepage_Serializer(serializers.ModelSerializer):
    institutes = CollaboratingInstituteSerializer(many=True, read_only=True)  # Use nested serializer

    class Meta:
        model = HomePage
        fields = '__all__'


class About_Serializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'
    

class CaseStudyThemeDescriptionSerializer(serializers.ModelSerializer):
    case_study_title = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudyThemeDescription
        fields = '__all__'

    def get_case_study_title(self, obj):
        return obj.case_study.study_area  # Assuming your Case_study model has a title field
    

class CaseStudyThemeImageSerializer(serializers.ModelSerializer):
    case_study_title = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudyThemeImage
        fields = '__all__'

    def get_case_study_title(self, obj):
        return obj.case_study.study_area  # Assuming your Case_study model has a title field



class Theme_Serializer(serializers.ModelSerializer):

    case_studies_description = CaseStudyThemeDescriptionSerializer(
        source='case_study_themes', many=True, read_only=True
    )

    case_studies_images = CaseStudyThemeImageSerializer(
        source='case_study_themes_image', many=True, read_only=True
    )
    
    class Meta:
        model = Theme
        fields = '__all__'


