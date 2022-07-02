from django.db import models

# Create your models here.
class Weather(models.Model): 
  created_at = models.DateField(auto_now_add=True)
  location = models.CharField(max_length=256)
  temperature = models.IntegerField()

  def __str__(self): 
    return (self.location + ': ' + str(self.temperature))