from django.db import models
from django.contrib.auth.models import User
class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    origin = models.ForeignKey(Place, related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey(Place, related_name='arrivals', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.flight_id}: {self.origin} to {self.destination}"

class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)