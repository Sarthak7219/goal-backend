from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Resources
from .models import TeamMember
from .models import Workshop
from .models import Case_study
from .serializer import ResourcesSerializer
from .serializer import WorkshopSerializer
from .serializer import TeamMemberSerializer
from .serializer import Case_studySerializer
from .models import *
from .serializer import *




def home_view(request):
    context = {}
    return render(request, 'index.html', context)

class CombinedDataView(APIView):
    def get(self, request):
        resources = Resources.objects.all()
        team_members = TeamMember.objects.all()
        workshops = Workshop.objects.all()
        case_studies = Case_study.objects.all()
        
        resources_serializer = ResourcesSerializer(resources, many=True)
        team_members_serializer = TeamMemberSerializer(team_members, many=True)
        workshops_serializer = WorkshopSerializer(workshops, many=True)
        case_studies_serializer = Case_studySerializer(case_studies, many=True)
        
        data = {
            'resources': resources_serializer.data,
            'team_members': team_members_serializer.data,
            'workshops': workshops_serializer.data,
            'case_studies': case_studies_serializer.data,
        }
        
        return Response(data)

def about_view(request):
    context = {}
    return render(request, 'about.html', context)


def case_studies_view(request):
    case_study_data = Case_study.objects.all()
    context = {
        'case_study_data':case_study_data,
    }
    return render(request, 'case_studies.html', context)

def resources_view(request):
    publications = Resources.objects.filter(category = 'publication')
    training_manuals = Resources.objects.filter(category = 'training_manual')

    context = {
        'publications':publications,
        'training_manuals':training_manuals,
    }
    return render(request, 'resources.html', context)


def team_view(request):
    
    collaborators = TeamMember.objects.filter(category = 'collaborator')
    research_associates = TeamMember.objects.filter(category = 'research_associate')
    community_trainers = TeamMember.objects.filter(category = 'community_trainer')
    interns = TeamMember.objects.filter(category = 'intern')
    students = TeamMember.objects.filter(category = 'student')

    context = {
        'collaborators':collaborators,
        'research_associates':research_associates,
        'community_trainers':community_trainers,
        'interns':interns,
        'students':students,
    }
    return render(request, 'team.html', context)

def gallery_view(request):
    context = {}
    return render(request, 'gallery.html', context)


def workshop_detail_view(request):
    context = {}
    if request.method == 'GET':
        workshop_id = request.GET.get('workshop_id')

        try:
            workshop = Workshop.objects.get(id = workshop_id)
            context['workshop']=workshop
        except:
            return HttpResponse('Workshop not found!')
   
    return render(request, 'workshop_detail.html', context)


def profile_detail_view(request):
    context = {
        # 'workshop_id':workshop_id
    }
    return render(request, 'profile_detail.html', context)


