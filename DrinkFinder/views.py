

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print "css/bootstrap.min.css"
    context_dict = {}
    context_dict['title'] = "Drink Finder - Welcome!"

    print context_dict
    return render(request, 'index.html', context_dict)