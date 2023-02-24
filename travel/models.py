from django.db import models

# Create your models here.



class Country(models.Model):
    class Meta:
        verbose_name_plural = "Coutries"
        
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class City(models.Model):
    class Meta:
        verbose_name_plural = 'Cities'
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    
 
    
class Agency(models.Model):
    class Meta:
        verbose_name_plural = "Agencies"
        
    name = models.CharField(max_length=100) 
    logo = models.ImageField('image', upload_to='company/', null=True, blank= True)
    
    def __str__(self):
        return f"({self.name})"
    
    
class Destination(models.Model):
    name = models.CharField(max_length=100)   
    image = models.ImageField('image', upload_to='destination/', null=True, blank= True)
 
    
    def __str__(self):
        return f"({self.name})"


class Trip(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True, related_name='trips')
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='trips')
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField('image', upload_to='trip/', null=True, blank= True)

    
    def __str__(self):
        return f"{self.destination} ({self.departure_date} to {self.return_date})"
    
    
class Traveler(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    image = models.ImageField('image', upload_to='traveler/', null=True, blank= True)
    
    def __str__(self):
        return f"({self.first_name}  {self.last_name})"



class Booking(models.Model):
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
    booking_time = models.DateTimeField(auto_now_add=True)
    
      
    
    def __str__(self):
        return f"({self.trip})"

    
