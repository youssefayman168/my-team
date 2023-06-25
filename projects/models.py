from django.db import models
from team.models import Section, Skill

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=120)
    member_name = models.CharField(max_length=120)
    client_name = models.CharField(max_length=120)
    finished_date = models.DateTimeField()
    skills = models.ManyToManyField(Skill)
    belongs_to = models.ForeignKey(Section, on_delete=models.CASCADE)
    project_photo = models.ImageField(upload_to="projects-photos/")
