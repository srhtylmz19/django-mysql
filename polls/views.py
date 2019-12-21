from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {'var1' : 'stands for variable 1'})
