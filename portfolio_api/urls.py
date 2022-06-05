"""portfolio_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from portfolio_api.quickstart import views

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"languages", views.LanguageViewSet)
router.register(r"projectlanguages", views.ProjectLanguageViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"jobs", views.JobViewSet)
router.register(r"hobbies", views.HobbyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
