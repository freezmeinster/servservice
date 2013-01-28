from django.shortcuts import render_to_response
from django.template import RequestContext
from employee.models import Employee,Office

def index(request):
    return render_to_response("employee/index.html",{
            "employees" : Employee.objects.all() 
        },context_instance=RequestContext(request))

def office_index(request):
    return render_to_response("employee/office_index.html",{
            "offices" : Office.objects.all() 
        },context_instance=RequestContext(request))