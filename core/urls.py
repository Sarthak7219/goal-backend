from django.urls import path
from .views import *


urlpatterns = [
    path('', CombinedDataView.as_view(), name='combined-data'),
    path('homepage_data/', get_homepage_data),
    path('about/', get_about_data),
    path('stories/', get_stories),
    path('team_members/', get_team_members),
    path('team_member_detail/', get_team_member_detail),
    path('workshops/', get_workshops),
    path('workshop_detail/', get_workshop_detail),
    path('case_studies/', get_case_studies),
    path('case_study_detail/', get_case_study_detail),
    path('resources/', get_resources),
    path('themes/', get_themes),
    path('theme_detail/', get_theme_detail),
    path('gallery/visit_photos/', get_visit_photos),
    path('gallery/workshop_photos/', get_workshop_photos),
    path('search/', search),
]