
from django.db import models
from employee.models import Employee

class Project(models.Model):
    nama_projek = models.CharField(max_length=255)
    tanggal_mulai = models.DateTimeField()
    tanggal_selesai = models.DateTimeField()
    project_manager = models.ForeignKey(Employee, related_name="project_manager")
    programmers = models.ManyToManyField(Employee, related_name="programmers")
    location = models.CharField(max_length=255)
    description = models.TextField()
    
