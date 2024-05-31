from django.urls import path
from .views import *


urlpatterns = [
    
path('', CombinedDataView.as_view(), name='combined-data'),
    # path('', home_view, name='home'),
  
    # path('about/', about_view, name='about' ),
    # path('case_studies/', case_studies_view, name='case_studies' ),
    # path('resources/', resources_view, name='resources' ),
    # path('team/', team_view, name='team' ),
    # path('gallery/', gallery_view, name='gallery' ),
    # # path('workshop/<workshop_id>', workshop_detail_view, name='workshop_detail'),   
    # path('workshop/', workshop_detail_view, name='workshop_detail'),   
    # path('profile/', profile_detail_view, name='profile_detail'),   
]