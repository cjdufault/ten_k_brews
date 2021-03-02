from django.shortcuts import render
from .models import Establishment, Drink


# Create your views here.
def home(request):
    return render(request, 'home.html')


def establishment_detail(request, establishment_pk):
    establishment = Establishment.objects.get(pk=establishment_pk)

    return render(request, 'establishment.html', {'establishment': establishment})


def browse_all(request):
    return render(request, 'list.html')


def browse_breweries(request):
    return render(request, 'list.html')


def browse_wineries(request):
    return render(request, 'list.html')


def browse_distilleries(request):
    return render(request, 'list.html')


def browse_cideries(request):
    return render(request, 'list.html')
