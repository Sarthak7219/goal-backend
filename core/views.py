from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resources
from django.http import FileResponse, Http404
from .models import TeamMember
from .models import Workshop
from .models import Case_study
from .serializer import ResourcesSerializer
from .serializer import WorkshopSerializer
from .serializer import TeamMemberSerializer
from .serializer import CaseStudySerializer
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
        image_case_study=Image_Case_Study.objects.all()
        image_workshop=Image_Workshop.objects.all()

        resources_serializer = ResourcesSerializer(resources, many=True, context={'request': self.request})
        team_members_serializer = TeamMemberSerializer(team_members, many=True)
        workshops_serializer = WorkshopSerializer(workshops, many=True)
        case_studies_serializer = CaseStudySerializer(case_studies, many=True)
        image_case_study_serializer=Image_Case_studys_Serializer(image_case_study,many=True)
        image_workshop_serializer=Image_Workshop_Serializer(image_workshop,many=True)
        data = {
            'resources': resources_serializer.data,
            'team_members': team_members_serializer.data,
            'workshops': workshops_serializer.data,
            'case_studies': case_studies_serializer.data,
            'image_case_study':image_case_study_serializer.data,
            'image_workshop':image_workshop_serializer.data
        }
        
        return Response(data)

class ImageCaseStudyList(generics.ListAPIView):
    queryset = Image_Case_Study.objects.all()
    serializer_class = Image_Case_studys_Serializer

    def get_serializer_context(self):
        return {'request': self.request}

class ImageWorkshopList(generics.ListAPIView):
    queryset = Image_Workshop.objects.all()
    serializer_class = Image_Workshop_Serializer

    def get_serializer_context(self):
        return {'request': self.request}
    

