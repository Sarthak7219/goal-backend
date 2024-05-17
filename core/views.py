from django.shortcuts import render
from .models import Case_study, Workshop

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
    context = {}
    return render(request, 'resources.html', context)


def team_view(request):
    context = {}
    return render(request, 'team.html', context)

def gallery_view(request):
    context = {}
    return render(request, 'gallery.html', context)


def workshop_detail_view(request, workshop_id):
    context = {
        'workshop_id':workshop_id
    }
    return render(request, 'workshop_detail.html', context)


