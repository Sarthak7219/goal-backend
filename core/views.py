from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import generics

def home_view(request):
    context = {}
    return render(request, 'index.html', context)

class CombinedDataView(APIView):
    def get(self, request):
        resources = Resources.objects.all()
        team_members = TeamMember.objects.all()
        workshops = Workshop.objects.all()
        case_studies = Case_study.objects.all()
        stories = Stories.objects.all()
        

        # Serialize data with request context
        resources_serializer = ResourcesSerializer(resources, many=True,context={'request': request})
        team_members_serializer = TeamMemberSerializer(team_members, many=True, context={'request': request})
        workshops_serializer = WorkshopSerializer(workshops, many=True)
        case_studies_serializer = CaseStudySerializer(case_studies, many=True)
        stories_serializer = Stories_Serializer(stories, many=True)
        

        data = {
            'resources': resources_serializer.data,
            'team_members': team_members_serializer.data,
            'workshops': workshops_serializer.data,
            'case_studies': case_studies_serializer.data,
            'stories': stories_serializer.data,
        }
        
        return Response(data)

class ImageCaseStudyList(generics.ListAPIView):
    queryset = Image_Case_Study.objects.all()
    serializer_class = Image_Case_studys_Serializer


class ImageWorkshopList(generics.ListAPIView):
    queryset = Image_Workshop.objects.all()
    serializer_class = Image_Workshop_Serializer
