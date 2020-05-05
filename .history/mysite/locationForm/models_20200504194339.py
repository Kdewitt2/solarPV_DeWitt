from django.db import models
from django.forms import ModelForm
from clientForm.models import Client
from datetime import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
was_published_recently.admin_order_field = 'pub_date'
was_published_recently.boolean = True
was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

#############################
#####Client from Dashboard####
#############################

class Location(models.Model):
    address1 = models.CharField(max_length=10)
    address2= models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    faxNumber = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['address1', 'address2', 'city', 'postalCode',
        'country', 'phoneNumber', 'faxNumber', 'client']
    address1 = models.CharField(max_length=10)
    address2= models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    faxNumber = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
