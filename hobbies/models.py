from django.db import models

# Create your models here.
class Hobby(models.Model):
    """
    Save details about hobbies and interests (what I do when I'm not working or coding!)
    """
    name = models.CharField(max_length=100)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name