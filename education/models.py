from unicodedata import name
from django.db import models
from sqlalchemy import true

# Create your models here.
class Course(models.Model):
  """ Save Course Info """
  name = models.CharField(max_length=100)
  school = models.CharField(max_length=100)
  school_url = models.URLField()
  certificate = models.BooleanField()
  certificate_image = models.URLField(null=true, blank=true)
  date_finished = models.DateField()
  description = models.TextField()

  def __str__(self):
      return self.name + " - " + self.school
  