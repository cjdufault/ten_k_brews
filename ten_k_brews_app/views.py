from django.shortcuts import render
from .models import Establishment, Drink


# Create your views here.
def home(request):
    return render(request, 'home.html')


# browse views
def browse_all(request):
    establishments = Establishment.objects.all().order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_breweries(request):
    establishments = \
        Establishment.objects.filter(type=Establishment.BREWERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_wineries(request):
    establishments = \
        Establishment.objects.filter(type=Establishment.WINERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_distilleries(request):
    establishments = \
        Establishment.objects.filter(type=Establishment.DISTILLERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


def browse_cideries(request):
    establishments = \
        Establishment.objects.filter(type=Establishment.CIDERY).order_by('name')
    return render(request, 'list.html', {'establishments': establishments})


# detail page views
def establishment_detail(request, establishment_pk):
    establishment = Establishment.objects.get(pk=establishment_pk)
    drinks = Drink.objects.filter(establishment=establishment)

    return render(request, 'establishment.html', {'establishment': establishment, 'drinks': drinks})


def drink_detail(request, drink_pk):
    drink = Drink.objects.get(pk=drink_pk)
    return render(request, 'drink.html', {'drink': drink})
