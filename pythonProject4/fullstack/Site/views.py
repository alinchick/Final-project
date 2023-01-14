from django.shortcuts import render
from .models import Pic_Vos,Pic_Geo
# Create your views here.
def home(request):
    return render(request,'Site/home.html')

def vostr(request):
    pic = Pic_Vos.objects.all()
    return render(request,'Site/vostr.html',{'pic': pic})

def geo(request):
    pic = Pic_Geo.objects.all()
    return render(request,'Site/geo.html',{'pic': pic})

def skills(request):
    return render(request,'Site/skills.html')