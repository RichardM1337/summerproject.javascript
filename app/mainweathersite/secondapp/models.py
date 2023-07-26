from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class weatherQuery(models.Model): #classes of database
    weather_text = models.CharField(max_length=200) #database fields
    pub_date = models.DateTimeField("date published") #"datetimefield" and "charfield" tells django about data type
    def __str__(self):  #shows well formatted object explanation when called
        return self.weather_text

class weatherInput(models.Model):
    question=models.ForeignKey(weatherQuery,on_delete=models.CASCADE) #"foreignkey" refers to relationship between input and query (one-to-one)
    choice_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self): 
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #check if date and time is greater than or equal to the timezone - the previous day's time
    
