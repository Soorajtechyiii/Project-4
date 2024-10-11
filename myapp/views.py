from django.shortcuts import render #type:ignore
from django.template import loader #type:ignore
from django.http import HttpResponse #type:ignore
def pagetml(request):
    id=loader.get_template('demo1.html')
    return HttpResponse(id.render())

    