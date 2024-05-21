from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home_view(request):
    context = {}
    return render(request, 'index.html', context)


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


