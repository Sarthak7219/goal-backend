from rest_framework import serializers
from .models import Resources, Case_study, Workshop, TeamMember, Image_Case_Study, Image_Workshop

class ResourcesSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Resources
        fields = '__all__'

   

class CaseStudySerializer(serializers.ModelSerializer):
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

class Image_Case_studys_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Image_Case_Study
        fields = '__all__'


class Image_Workshop_Serializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image_Workshop
        fields = '__all__'

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if request is not None:
    #         return request.build_absolute_uri(obj.image.url)
    #     return obj.image.url
