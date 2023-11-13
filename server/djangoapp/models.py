from django.db import models
from django.utils.timezone import now
import json

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + ", " + "Description: " + self.description

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)
    id = models.IntegerField(default=1,primary_key=True)

    # Choices for the car_type field as tuples
    TYPE_CHOICES = [
        ('Sedan', "Sedan"),
        ('SUV', "SUV"),
        ('Wagon', "Wagon")
    ]

    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default='Sedan'
    )

    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + ", " \
               "Carmake: " + str(self.carmake) + ", " \
               "Type: " + self.car_type + ", " \
               "Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Dealership: " + self.dealership + \
               "Name: " + self.name + \
               "Purchase: " + self.purchase + \
               "Review: " + self.review + \
               "Purchase date: " + str(self.purchase_date) + \
               "Car Make: " + self.car_make + \
               "Car Model: " + self.car_model + \
               "Car Year: " + str(self.car_year) + \
               "Sentiment: " + self.sentiment + \
               "id: " + str(self.id)
