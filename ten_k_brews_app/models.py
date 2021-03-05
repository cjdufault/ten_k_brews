from django.db import models


# Create your models here.
class Establishment(models.Model):

    # choices for establishment types
    BREWERY = 'Brewery'
    WINERY = 'Winery'
    DISTILLERY = 'Distillery'
    CIDERY = 'Cidery'
    OTHER = 'Other'

    ESTABLISHMENT_TYPES = (
        (BREWERY, 'Brewery'),   # (actual value, human readable value)
        (WINERY, 'Winery'),
        (DISTILLERY, 'Distillery'),
        (CIDERY, 'Cidery'),
        (OTHER, 'Other')
    )

    # descriptive variables
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=10000, blank=True)
    type = models.CharField(max_length=10, choices=ESTABLISHMENT_TYPES, blank=False)

    # location variables
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip_code = models.CharField(max_length=5, blank=False)

    def __str__(self):
        return f'{self.name} -- {self.type} -- {self.city}'


class Drink(models.Model):

    # choices for drink types
    BEER = 'Beer'
    WINE = 'Wine'
    LIQUOR = 'Liquor'
    CIDER = 'Cider'
    OTHER = 'Other'

    DRINK_TYPES = (
        (BEER, 'Beer'),
        (WINE, 'Wine'),
        (LIQUOR, 'Liquor'),
        (CIDER, 'Cider'),
        (OTHER, 'Other')
    )

    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=10, choices=DRINK_TYPES, blank=False)
    style = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=10000, blank=True)

    # what establishment makes this drink? drinks deleted when their establishment has been deleted due to CASCADE
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    def __str__(self):
        string = f'{self.name} -- {self.type}'

        if self.style is not None:
            string += f' -- {self.style}'

        return string
