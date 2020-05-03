from django.db import models
from django.forms import ModelForm

#############################
#####Client from Dashboard####
#############################

class Client (models.Model):
    clientCode = models.CharField(max_length=8)
    clientName = models.CharField(max_length=10)
    clientType = models.CharField(max_length=10)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['clientCode', 'clientName', 'clientType']
