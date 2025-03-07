from rest_framework import serializers
from .models import *
import re


class CollaboratingInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratingInstitute
        fields = ['name', 'logo']

class CaseStudiesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Case_study
        fields =  ['id', 'country', 'study_area', 'thumbnail']
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        else:
            return None

class WorkshopsSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Workshop
        fields =  ['id', 'title', 'venue', 'formatted_date', 'thumbnail']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        else:
            return None

class Home_Gallery(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image_Case_Study
        fields =  ['image', 'caption', 'formatted_date']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None

class Homepage_Serializer(serializers.ModelSerializer):
    institutes = CollaboratingInstituteSerializer(many=True, read_only=True)  # Foriegn key relation
    gallery_photos = serializers.SerializerMethodField()
    map_image = serializers.SerializerMethodField()

    class Meta:
        model = HomePage
        fields = ['map_image', 'institutes', 'gallery_photos']
    
    def get_gallery_photos(self, obj):
        request = self.context.get('request')
        gallery_photos = Image_Case_Study.objects.all()[:8]
        serializer = Home_Gallery(gallery_photos, many=True, context={'request': request})
        return serializer.data
    def get_map_image(self, obj):
        request = self.context.get('request')
        if obj.map_image:
            if request:
                return request.build_absolute_uri(obj.map_image.url)
            return obj.map_image.url
        else:
            return None

class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['abstract', 'description', 'img1', 'img2', 'img3', 'img4']
    
class Stories_Serializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Stories
        fields = ['description', 'location', 'date', 'link', 'thumbnail']

    def get_thumbnail(self, obj):
        if obj.link:
            pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
            match = re.search(pattern, obj.link)
            if match:
                video_id = match.group(1)
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
                return thumbnail_url
            else:
                return None
        else:
            return None

class TeamMembersSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = TeamMember
        fields = ['id','category','name','position','organisation','image']
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None

class TeamMemberDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = TeamMember
        fields = '__all__'
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None

class ResourcesSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    class Meta:
        model = Resources
        fields = ['id', 'title','formatted_date','publisher','link','pdf', 'category']
    def get_formatted_date(self, obj):
        return obj.date_of_publishing.strftime("%d %b %y") if obj.date_of_publishing else None

class ImageCaseStudySerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image_Case_Study
        fields = ['image', 'caption', 'formatted_date']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None
        
class ImageWorkshopSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = Image_Workshop
        fields = ['image', 'caption', 'formatted_date']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None

class WorkshopDetailSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    workshop_photos = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Workshop
        fields = ['id', 'title','formatted_date','venue','description','organised_by','link','speakers','key_takeaways','mode', 'thumbnail', 'workshop_photos']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    
    def get_workshop_photos(self, obj):
        photos = obj.images.all()[:4]
        request = self.context.get('request')
        serializer = ImageWorkshopSerializer(photos, many=True, context={'request': request})
        return serializer.data
    
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:        
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        else:
            return None

class CaseStudyDetailSerializer(serializers.ModelSerializer):
    related_workshops = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Case_study
        fields = ['id', 'country', 'study_area', 'description','related_workshops', 'photos']

    def get_related_workshops(self, obj):
        workshops = obj.get_all_workshops()
        request = self.context.get('request')
        serializer = WorkshopsSerializer(workshops, many=True, context={'request': request})
        return serializer.data
    
    def get_photos(self, obj):
        photos = obj.images.all()[:4]
        request = self.context.get('request')
        serializer = ImageCaseStudySerializer(photos, many=True, context={'request': request})
        return serializer.data
    
class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'title']

class CaseStudyThemeDescriptionSerializer(serializers.ModelSerializer):
    study_area = serializers.SerializerMethodField()
    class Meta:
        model = CaseStudyThemeDescription
        fields = ['case_study', 'study_area', 'description']
    def get_study_area(self, obj):
        return obj.case_study.study_area
    
class CaseStudyThemeImageSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = CaseStudyThemeImage
        fields = ['case_study', 'image', 'caption', 'formatted_date']
    def get_formatted_date(self, obj):
        return obj.date.strftime("%d %b %y") if obj.date else None
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        else:
            return None

class ThemeDetailSerializer(serializers.ModelSerializer):
    case_studies = serializers.SerializerMethodField()
    class Meta:
        model = Theme
        fields = ['id', 'title', 'description', 'case_studies']

    def get_case_studies(self, obj):
        case_study_dict = {}

        descriptions = CaseStudyThemeDescription.objects.filter(theme=obj)
        descriptions_data = CaseStudyThemeDescriptionSerializer(descriptions, many=True).data
        request = self.context.get('request')
        images = CaseStudyThemeImage.objects.filter(theme=obj)
        images_data = CaseStudyThemeImageSerializer(images, many=True, context={'request': request}).data

        for desc in descriptions_data:
            case_study_id = desc['case_study']
            if case_study_id not in case_study_dict:
                case_study_dict[case_study_id] = {'case_study': desc['study_area'], 'description': desc['description'], 'images': []}

        for img in images_data:
            case_study_id = img['case_study']
            if case_study_id not in case_study_dict:
                case_study_dict[case_study_id] = {'case_study': case_study_id, 'descriptions': [], 'images': []}
            case_study_dict[case_study_id]['images'].append(img)

        return list(case_study_dict.values())







