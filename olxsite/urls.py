from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from olx import settings
from olxsite import views

urlpatterns = [
    path('', views.showmainpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)