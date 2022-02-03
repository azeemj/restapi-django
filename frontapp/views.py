from django.shortcuts import render
import datetime

# Create your views here.
from django.utils.safestring import SafeString

from .service.service import get_droplets


def inventory(request):
    data = get_droplets(0)
    context = {
        'inventory_list': data
    }
    return render(request, 'list.html', context)


def detail(request, para):
    data = get_droplets(para)
    print('test', data)
    context = {
        'inventory_details': data
    }
    return render(request, 'details.html', context)
