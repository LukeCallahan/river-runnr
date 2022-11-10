from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
    'id': '1',
    'title': "Ecommerce Website",
    'description': 'Fully functional ecommerce website'
    },
    {
    'id': '2',
    'title': "Portfolio Website",
    'description': 'This is a project where I built out my portfolio'
    },
    {
    'id': '1',
    'title': "Social Network",
    'description': 'Awesome open source project I am still working on.'
    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html')
