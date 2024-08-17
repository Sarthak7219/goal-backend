from django.urls import path
from .views import *


urlpatterns = [
    
path('', CombinedDataView.as_view(), name='combined-data'),
path('casestudy_images/', ImageCaseStudyList.as_view(), name='images-casestudy'),
path('workshop_images/', ImageWorkshopList.as_view(), name='images-workshop'),
path('themes/', ThemeListCreateAPIView.as_view(), name='theme-list-create'),

]