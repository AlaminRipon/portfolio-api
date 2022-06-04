from asyncio import constants
from operator import mod
from django.db import models
from education.models import Course


# Create your models here.
class Language(models.Model):
  """ Save language details """
  name = models.CharField(max_length=100)
  link = models.URLField()
  logo = models.URLField()

  def __str__(self):
    return self.name
  

class Project(models.Model):
  """ Save project details """
  PROJECT_TYPE_CHOICES = [
    ('TUT', 'Tutorial'),
    ('COU', 'Graded Coursework'),
    ('IND', 'Individual Project'),
    ('COM', 'Commission'),
  ]
  
  title = models.CharField(max_length=100)
  live_link = models.URLField()
  code_link = models.URLField()
  preview_img = models.URLField()
  type = models.CharField(max_length=3, choices=PROJECT_TYPE_CHOICES, default='IND')
  course = models.ForeignKey(Course, blank=True, null=True, related_name='projects', on_delete=models.SET_NULL)
  description = models.TextField()
  description_nl = models.TextField(default="Beschrijving binnenkort beschikbaar!")
  languages = models.ManyToManyField(Language, through='ProjectLanguage', related_name="projects")
  
  def __str__(self):
    return self.title
  
  

class ProjectLanguage(models.Model):
  """ Connect Project Model to Language model"""
  class Meta:
    """
    Ensure each project/language pairing can only be added to each list once 
    """
    constraints = [models.UniqueConstraint(fields=["project", "language"], name='unique_pairing')]
  
  project = models.ForeignKey(Project, related_name="project_languages", on_delete=models.CASCADE)
  language = models.ForeignKey(Language, related_name="project_languages", on_delete=models.CASCADE)

  def __str__(self):
    return self.project.title + " - " + self.language.name





