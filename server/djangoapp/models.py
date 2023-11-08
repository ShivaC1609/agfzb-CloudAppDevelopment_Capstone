from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='car name')
    description = models.TextField
    producer = models.CharField

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car')
   
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MINIVAN = 'Minivan'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MINIVAN, 'Minivan')
    ]

    type = models.CharField(
        null=False,
        max_length=50,
        choices=CAR_TYPES,
        default=SEDAN
    )
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    year = models.DateField(default=now)

    def __str__(self):
        return "Name: " + self.name

#class CarModel(models.Model):
#   car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
#    name = models.CharField(null=False, max_length=100)
#    dealer_id = models.IntegerField(primary_key=True, default=1)
#   year = models.DateField(default=now)
#
#    SEDAN = "Sedan"
#    SUV = "SUV"
#    WAGON = "Station wagon"
#    SPORT = "Sports car"
#    BIKE = "Motor bike"
#    SCOOTER = "Scooter"
#    OTHER = "Other"
#    CAR_CHOICES = [
#        (SEDAN, "Sedan"), 
#        (SUV, "SUV"),
#        (WAGON, "Station wagon"),
#        (SPORT, "Sports Car"),
#        (BIKE, "Motor bike"),
#        (SCOOTER, "Scooter"),
#        (OTHER, 'Other')]
#    car_type = models.CharField(null=False, max_length=15, choices=CAR_CHOICES, default=SEDAN)
#
#   def __str__(self):
#        "name : " + self.name + "," + \
#        "dealer : " + self.dealer_id + "," + \
#        "year : " + self.year + "," + \
#        "type : " + self.car_type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
