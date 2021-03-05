from django.shortcuts import render, redirect, get_object_or_404
from .models import Establishment, Drink
from .forms import NewDrinkForm


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
    establishment = get_object_or_404(Establishment, pk=establishment_pk)
    drinks = Drink.objects.filter(establishment=establishment)

    return render(request, 'establishment.html', {'establishment': establishment, 'drinks': drinks})


def drink_detail(request, drink_pk):
    drink = get_object_or_404(Drink, pk=drink_pk)
    return render(request, 'drink.html', {'drink': drink})


# forms
def new_drink_form(request, establishment_pk):

    establishment = get_object_or_404(Establishment, pk=establishment_pk)

    # receive new Drink data from form
    if request.method == 'POST':
        form = NewDrinkForm(request.POST, request.FILES)

        if form.is_valid():
            drink = form.save(commit=False)
            drink.establishment = establishment
            drink.save()
            return redirect('drink_detail', drink_pk=drink.pk)

    # show form to receive input
    else:
        form = NewDrinkForm()

    return render(request, 'new_drink.html', {'form': form, 'establishment': establishment})

