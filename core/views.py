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
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class CombinedDataView(APIView):
    def get(self, request):
        return Response({"HI"})

@api_view(['GET'])
def get_homepage_data(request):
    cache_key = 'homepage_data'
    cache_data = cache.get(cache_key)
    if cache_data is None:
        homepage_data = HomePage.objects.first()
        if homepage_data:
            serializer = Homepage_Serializer(homepage_data, context={'request': request})
            cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
            return Response(serializer.data)
        return Response({"error": "No homepage data found"}, status=404)
    return Response(cache_data)

@api_view(['GET'])
def get_about_data(request):
    cache_key = 'about_data'
    cache_data = cache.get(cache_key)
    if cache_data is None:
        about_data = About.objects.first()
        if about_data:
            serializer = About_Serializer(about_data)
            cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
            return Response(serializer.data)
        return Response({"error": "No about data found"}, status=404)
    return Response(cache_data)

@api_view(['GET'])
def get_stories(request):
    cache_key = 'stories_data'
    cache_data = cache.get(cache_key)
    if cache_data is None:
        stories = Stories.objects.all()
        if stories:
            serializer = Stories_Serializer(stories, many=True)
            cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
            return Response(serializer.data)
        return Response({"error": "No stories found"}, status=404)
    return Response(cache_data)

@api_view(['GET'])
def get_team_members(request):
    cache_key = 'team_data'
    cache_data = cache.get(cache_key)
    if cache_data is None:
        team_members = TeamMember.objects.all()
        if team_members:
            serializer = TeamMembersSerializer(team_members, many=True, context={'request': request})
            cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
            return Response(serializer.data)
        return Response({"error": "No team member found"}, status=404)
    return Response(cache_data)

@api_view(['POST'])
def get_team_member_detail(request):
    id = request.data.get('id')
    if not id:
        return Response({"error": "ID is required"}, status=400)
    cache_key = f"team_member_{id}"
    cache_data = cache.get(cache_key)

    if cache_data is not None:
        return Response(cache_data)
    try:
        member = TeamMember.objects.get(id=id)
        serializer = TeamMemberDetailSerializer(member, context={'request': request})
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data)
    except TeamMember.DoesNotExist:
        return Response({"error": "Team member not found"}, status=404)


@api_view(['GET'])
def get_workshops(request):
    cache_key = "workshops_list"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    workshops = Workshop.objects.order_by('-date')
    serializer = WorkshopsSerializer(workshops, many=True, context={'request': request})
    cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
    return Response(serializer.data)

@api_view(['POST'])
def get_workshop_detail(request):
    id = request.data.get('id')
    if not id:
        return Response({"error": "ID is required"}, status=400)
    cache_key = f"workshop_{id}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    try:
        workshop = Workshop.objects.get(id=id)
        serializer = WorkshopDetailSerializer(workshop, context={'request': request})
        cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data)
    except Workshop.DoesNotExist:
        return Response({"error": "Workshop not found"}, status=404)


@api_view(['GET'])
def get_case_studies(request):
    cache_key = "case_studies_list"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    case_studies = Case_study.objects.all()
    serializer = CaseStudiesSerializer(case_studies, many=True, context={'request': request})
    cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
    return Response(serializer.data)

@api_view(['POST'])
def get_case_study_detail(request):
    id = request.data.get('id')
    if not id:
        return Response({"error":"ID is required"},status=400)
    cache_key = f"case_study_{id}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    try:
        case_study = Case_study.objects.get(id=id)
        serializer = CaseStudyDetailSerializer(case_study,context={'request':request})
        cache.set(cache_key,serializer.data,timeout=CACHE_TTL)
        return Response(serializer.data)
    except Case_study.DoesNotExist:
        return Response({"error":"Case Study not found"},status=404)


@api_view(['GET'])
def get_resources(request):
    cache_key = "resources_list"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    resources = Resources.objects.all()
    grouped_data = defaultdict(list)
    serializer = ResourcesSerializer(resources, many=True)
    for resource in serializer.data:
        grouped_data[resource["category"]].append(resource)
    cache.set(cache_key, grouped_data, timeout=CACHE_TTL)
    return Response(grouped_data)


@api_view(['GET'])
def get_themes(request):
    cache_key = "themes_list"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    themes = Theme.objects.all()
    serializer = ThemesSerializer(themes, many=True)
    cache.set(cache_key, serializer.data, timeout=CACHE_TTL)
    return Response(serializer.data)


@api_view(['POST'])
def get_theme_detail(request):
    id = request.data.get('id')
    if not id:
        return Response({"error":"ID is required"},status=400)
    cache_key = f"theme_{id}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    try:
        theme = Theme.objects.get(id=id)
        serializer = ThemeDetailSerializer(theme,context={'request':request})
        cache.set(cache_key,serializer.data,timeout=CACHE_TTL)
        return Response(serializer.data)
    except Theme.DoesNotExist:
        return Response({"error":"Theme not found"},status=404)


@api_view(['POST'])
def get_visit_photos(request):
    id = request.data.get('id')
    page_number = request.query_params.get("page", 1)
    if not id:
        return Response({"error":"ID is required"},status=400)
    cache_key = f"visit_photos_{id}_page_{page_number}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    try:
        case_study = Case_study.objects.get(id=id)
        visit_photos_data = case_study.images.all().order_by('-date')
        paginator = PageNumberPagination()
        paginator.page_size = 8
        result_page = paginator.paginate_queryset(visit_photos_data, request)
        serializer = ImageCaseStudySerializer(result_page,many=True,context={'request':request})
        response = paginator.get_paginated_response(serializer.data)
        cache.set(cache_key, response.data, timeout=CACHE_TTL)
        return response
    except Case_study.DoesNotExist:
        return Response({"error":"Case Study not found"},status=404)


@api_view(['POST'])
def get_workshop_photos(request):
    id = request.data.get('id')
    page_number = request.query_params.get("page", 1)
    if not id:
        return Response({"error":"ID is required"},status=400)
    cache_key = f"workshop_photos_{id}_page_{page_number}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    try:
        case_study = Case_study.objects.get(id=id)
        workshop_photos_data = Image_Workshop.objects.filter(workshop__case_study=case_study).order_by('-date')
        paginator = PageNumberPagination()
        paginator.page_size = 8
        result_page = paginator.paginate_queryset(workshop_photos_data, request)
        serializer = ImageWorkshopSerializer(result_page,many=True,context={'request':request})
        response = paginator.get_paginated_response(serializer.data)
        cache.set(cache_key, response.data, timeout=CACHE_TTL)
        return response
    except Case_study.DoesNotExist:
        return Response({"error":"Case Study not found"},status=404)


@api_view(['GET'])
def search(request):
    query = request.query_params.get('query', '').strip()
    if not query:
        return Response({"error":"Query parameter is required"},status=400)
    cache_key = f"search_results_{query}"
    cache_data = cache.get(cache_key)
    if cache_data is not None:
        return Response(cache_data)
    case_studies = Case_study.objects.filter(study_area__icontains=query)
    workshops = Workshop.objects.filter(title__icontains=query)
    themes = Theme.objects.filter(title__icontains=query)
    results = []
    for workshop in workshops:
        results.append({"type":"workshop","title":workshop.title,"id":workshop.id})
    for case_study in case_studies:
        results.append({"type":"case_study","title":case_study.study_area,"id":case_study.id})
    for theme in themes:
        results.append({"type":"theme","title":theme.title,"id":theme.id})
    response_data = {"results":results}
    cache.set(cache_key, response_data, timeout=CACHE_TTL)
    return Response(response_data)

