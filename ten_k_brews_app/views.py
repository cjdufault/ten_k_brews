from django.shortcuts import render
from .models import Establishment


# Create your views here.
def home(request):
    return render(request, 'home.html')


def establishment_detail(request, establishment_pk):
    establishment = Establishment.objects.get(pk=establishment_pk)
    return render(request, 'establishment.html', {'establishment': establishment})


def browse_all(request):
    establishments = Establishment.objects.all().order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_breweries(request):
    establishments = \
        Establishment.objects.filter(establishment_type=Establishment.BREWERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_wineries(request):
    establishments = \
        Establishment.objects.filter(establishment_type=Establishment.WINERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_distilleries(request):
    establishments = \
        Establishment.objects.filter(establishment_type=Establishment.DISTILLERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_cideries(request):
    establishments = \
        Establishment.objects.filter(establishment_type=Establishment.CIDERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})
