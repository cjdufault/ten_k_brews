from django.shortcuts import render, redirect, get_object_or_404
from .models import Establishment, Drink
from .forms import EstablishmentSearchForm, NewDrinkForm


# Create your views here.
def home(request):
    search_form = EstablishmentSearchForm
    return render(request, 'home.html', {'search_form': search_form})


# browse views
def browse(request, type_filter):
    search_form = EstablishmentSearchForm

    if type_filter == 'all':
        establishments = Establishment.objects.all().order_by('name')
    elif type_filter == 'breweries':
        establishments = Establishment.objects.filter(type=Establishment.BREWERY).order_by('name')
    elif type_filter == 'wineries':
        establishments = Establishment.objects.filter(type=Establishment.WINERY).order_by('name')
    elif type_filter == 'distilleries':
        establishments = Establishment.objects.filter(type=Establishment.DISTILLERY).order_by('name')
    elif type_filter == 'cideries':
        establishments = Establishment.objects.filter(type=Establishment.CIDERY).order_by('name')
    else:
        return redirect('home')

    return render(request, 'list.html', {'establishments': establishments, 'search_form': search_form})


def search(request):
    search_form = EstablishmentSearchForm
    search_term = request.GET.get('search_term')

    if search_term:
        establishments = Establishment.objects.filter(name__icontains=search_term).order_by('name')
        return render(request, 'list.html', {'establishments': establishments, 'search_form': search_form})

    return redirect('home')


# detail page views
def establishment_detail(request, establishment_pk):
    search_form = EstablishmentSearchForm

    establishment = get_object_or_404(Establishment, pk=establishment_pk)
    drinks = Drink.objects.filter(establishment=establishment).order_by('name')

    return render(request, 'establishment.html',
                  {'establishment': establishment, 'drinks': drinks, 'search_form': search_form})


def drink_detail(request, drink_pk):
    search_form = EstablishmentSearchForm
    drink = get_object_or_404(Drink, pk=drink_pk)
    return render(request, 'drink.html', {'drink': drink, 'search_form': search_form})


# forms
def new_drink_form(request, establishment_pk):
    search_form = EstablishmentSearchForm
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

    return render(request, 'new_drink.html', {'form': form, 'establishment': establishment, 'search_form': search_form})
