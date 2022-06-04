from django.contrib.auth.models import User, Group
from rest_framework import serializers

# From own apps
from codeprojects.models import Language, Project, ProjectLanguage
from education.models import Course
from experience.models import Job
from hobbies.models import Hobby


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["url", "title", "live_link", "code_link", "preview_img", "type", "course", "description", "description_nl"]

        
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ["url", "name", "link", "logo", "projects"]
        

class ProjectLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectLanguage
        fields = ["url", "project", "language"]
        

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["url", "name", "school", "school_url", "certificate", "certificate_image", "date_finished", "description"]


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ["url", "title", "company_name", "company_link", "company_logo", "type", "description", "start_date", "end_date", "code_related"]


class HobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hobby
        fields = ["url", "name", "image", "description"]