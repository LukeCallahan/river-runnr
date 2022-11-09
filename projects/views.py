from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our Projects')

def project(request, pk):
    return HttpResponse('This is a single project ' + str(pk))
