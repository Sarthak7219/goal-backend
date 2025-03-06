from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from collections import defaultdict
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.pagination import PageNumberPagination

def home_view(request):
    context = {}
    return render(request, 'index.html', context)

class CombinedDataView(APIView):
    def get(self, request):
        return Response({"HI"})

class ImageCaseStudyList(generics.ListAPIView):
    queryset = Image_Case_Study.objects.all()
    serializer_class = ImageCaseStudySerializer


@api_view(['GET'])
def get_homepage_data(request):
    homepage_data = HomePage.objects.first()
    serializer = Homepage_Serializer(homepage_data, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_about_data(request):
    about_data = About.objects.first()
    serializer = About_Serializer(about_data)
    return Response(serializer.data)

@api_view(['GET'])
def get_stories(request):
    stories = Stories.objects.all()
    serializer = Stories_Serializer(stories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_team_members(request):
    team_members = TeamMember.objects.all()
    serializer = TeamMembersSerializer(team_members, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def get_team_member_detail(request):
    try:
        id = request.data.get('id')
        member = TeamMember.objects.get(id = id)
    except:
        return Response({"error": "Team member not found"})
    serializer = TeamMemberDetailSerializer(member, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_workshops(request):
    workshops = Workshop.objects.order_by('-date')
    serializer = WorkshopsSerializer(workshops, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def get_workshop_detail(request):
    try:
        id = request.data.get('id')
        workshop = Workshop.objects.get(id = id)
    except:
        return Response({"error": "Workshop not found"})
    serializer = WorkshopDetailSerializer(workshop, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_case_studies(request):
    case_studies = Case_study.objects.all()
    serializer = CaseStudiesSerializer(case_studies, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def get_case_study_detail(request):
    try:
        id = request.data.get('id')
        case_study = Case_study.objects.get(id = id)
    except:
        return Response({"error": "Case Study not found"})
    serializer = CaseStudyDetailSerializer(case_study, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_resources(request):
    resources = Resources.objects.all()
    grouped_data = defaultdict(list)
    serializer = ResourcesSerializer(resources, many=True)
    for resource in serializer.data:
        grouped_data[resource["category"]].append(resource)
    return Response(grouped_data)

@api_view(['GET'])
def get_themes(request):
    themes = Theme.objects.all()
    serializer = ThemesSerializer(themes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_theme_detail(request):
    try:
        id = request.data.get('id')
        theme = Theme.objects.get(id = id)
    except:
        return Response({"error": "Theme not found"})
    serializer = ThemeDetailSerializer(theme, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def get_visit_photos(request):
    try:
        id = request.data.get('id')
        case_study = Case_study.objects.get(id = id)
    except:
        return Response({"error": "Case Study not found"})
    visit_photos_data = case_study.images.all().order_by('-date')
    paginator = PageNumberPagination()
    paginator.page_size = 8

    result_page = paginator.paginate_queryset(visit_photos_data, request)
    serializer = ImageCaseStudySerializer(result_page, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def get_workshop_photos(request):
    try:
        id = request.data.get('id')
        case_study = Case_study.objects.get(id = id)
    except:
        return Response({"error": "Case Study not found"})
    workshop_photos_data = Image_Workshop.objects.filter(workshop__case_study=case_study).order_by('-date')
    paginator = PageNumberPagination()
    paginator.page_size = 8

    result_page = paginator.paginate_queryset(workshop_photos_data, request)
    serializer = ImageWorkshopSerializer(result_page, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def search(request):
    query = request.query_params.get('query', '')
    case_studies = Case_study.objects.filter(study_area__icontains = query)
    workshops = Workshop.objects.filter(title__icontains = query)
    themes = Theme.objects.filter(title__icontains = query)
    
    results = []
    for workshop in workshops:
        results.append({"type": "workshop", "title": workshop.title, "id" : workshop.id})
    for case_study in case_studies:
        results.append({"type": "case_study", "title": case_study.study_area, "id" : case_study.id})
    for theme in themes:
        results.append({"type": "theme", "title": theme.title, "id" : theme.id})

    return Response({"results": results})
