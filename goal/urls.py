from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# from .views import index_view
# from django.urls import path, re_path
# from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
    path('', include('core.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 