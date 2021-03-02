from django.db import models

# Create your models here.


class Establishment(models.Model):

    # enumerates options for type of establishment, e.g. Establishment.EstablishmentType.BREWERY == 1
    class EstablishmentType(models.IntegerChoices):
        BREWERY = 1
        WINERY = 2
        DISTILLERY = 3
        CIDERY = 4
        OTHER = 5

    # descriptive variables
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=500, blank=True)
    establishment_type = models.IntegerField(choices=EstablishmentType.choices)

    # location variables
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip_code = models.CharField(max_length=5, blank=False)

    def __str__(self):
        return f'{self.name} ({self.city})'

