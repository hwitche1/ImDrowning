from django.contrib import admin
from django.urls import path
from django.views.generic import *

class Index(TemplateView):
    template_name = "index.html"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='index'),
]
