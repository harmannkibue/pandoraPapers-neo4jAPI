from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    re_path(r'^fetch/', include('fetch_api.urls', name='fetch_api')),
    re_path(r'^fetch/', include('fetch_api.urls')),
]
