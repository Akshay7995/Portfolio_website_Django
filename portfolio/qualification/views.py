from django.shortcuts import render,get_object_or_404
from .models import Qualification

# Create your views here.
def intro(request):
    qualifications = Qualification.objects
    return render(request,'qualification/home.html',{'qualifications':qualifications})

def detail(request,qualification_id):
    qualification_detail = get_object_or_404(Qualification,pk=qualification_id)
    return render(request,'qualification/detail.html',{'qualification':qualification_detail})