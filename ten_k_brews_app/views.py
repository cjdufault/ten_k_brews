from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


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
