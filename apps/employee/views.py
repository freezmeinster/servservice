from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

def index(request):
    return render_to_response("employee/index.html",{
            "users" : User.objects.all() 
        },context_instance=RequestContext(request))