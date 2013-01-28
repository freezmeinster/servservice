from django.db import models
from django.contrib.auth.models import User

class Office(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    
class Employee(User):
    EMP = (
        ("pm","Project Manager"),
        ("n","NOC"),
        ("p","Programer"),
    )
    
    position = models.CharField(max_length=2,choices=EMP)
    office = models.ForeignKey(Office)
    phone = models.CharField(max_length=20)