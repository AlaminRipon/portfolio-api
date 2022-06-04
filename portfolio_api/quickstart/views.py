from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from portfolio_api.quickstart.serializers import (
    UserSerializer,
    GroupSerializer,
    LanguageSerializer,
    ProjectSerializer,
    ProjectLanguageSerializer,
    CourseSerializer,
    JobSerializer,
    HobbySerializer
)
from codeprojects.models import Language, Project, ProjectLanguage
from education.models import Course
from experience.models import Job
from hobbies.models import Hobby


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectLanguageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = ProjectLanguage.objects.all()
    serializer_class = ProjectLanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be viewed or edited
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]


class HobbyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hobbies to be viewed or edited
    """
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer
    permission_classes  = [permissions.IsAuthenticatedOrReadOnly]