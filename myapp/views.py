from django.shortcuts import render #type:ignore
from django.template import loader #type:ignore
from django.http import HttpResponse #type:ignore
from.models import student #type:ignore
def pagetml(request):
    id=loader.get_template('demo1.html')
    return HttpResponse(id.render())
def fsave(request):
    if request.method =='POST':
        name=request.POST.get('t1')
        username=request.POST.get('t2')
        password=request.POST.get('t3')
        phonenumber=request.POST.get('t4')
        place=request.POST.get('t5')
        s=student(name=name,username=username,password=password,phonemnumber=phonenumber,place=place)
        s.save()
        return HttpResponse('data saved')
    else:
        return HttpResponse('data not saved')


    
    

    