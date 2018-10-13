from django.shortcuts import render,render_to_response

# Create your views here.
from tool.models import *

from django.http import HttpResponse

def index(request):
    context = {}
    if request.POST:
        context['building_name'] = request.POST['building_name']
        context['week'] = request.POST['week']
    return render(request,'index.html')
def classroom(request):
    building_name = request.POST['building_name']
    week = request.POST['week'] 

    building = ''

    if '分区教学' in building_name:
        building = '分区教学'
        if 'A' in building_name:
            building_name = 'A'
        elif 'B' in building_name:
            if '东' in building_name:
                building_name = 'B东'
            elif '西' in building_name:
                building_name = 'B西'
        elif 'C' in building_name:
            building_name = 'C'
        elif 'D' in building_name:
            building_name = 'D'
        elif '东阶' in building_name:
            building_name = '东阶'
        elif '西阶' in building_name:
            building_name = '西阶'
    elif '实训楼' in building_name:
        building = '实训楼'
        if 'A' in building_name:
            building_name = 'A'
        elif 'B' in building_name:
            building_name = 'B'

    if week == "星期一":
        info = Monday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期二":
        info = Tuesday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期三":
        info = Wednesday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期四":
        info = Thursday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期五":
        info = Friday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期六":
        info = Saturday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    elif week =="星期日":
        info = Sunday.objects.filter(classroom__contains=building).filter(classroom__contains=building_name)
    return render_to_response('search.html',{'info':info})

