from django.db import models
import datetime
from django.utils import timezone
from django.forms import ModelForm


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
#####Models for Dashboard####
#############################

class Client (models.Model):
    clientCode = models.CharField(max_length=8)
    clientName = models.CharField(max_length=10)
    clientType = models.CharField(max_length=10)

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['clientCode', 'clientName', 'clientType']

class Product(models.Model):
    prodName = models.CharField(max_length=20)
    cellTech = models.CharField(max_length=20)
    cellManuf = models.CharField(max_length=20)
    numCells = models.CharField(max_length=20)
    numCellsSeries = models.CharField(max_length=20)
    numSeriesStrings = models.CharField(max_length=20)
    numDiodes = models.CharField(max_length=20)
    prodLength = models.CharField(max_length=20)
    prodWidth = models.CharField(max_length=20)
    superstrateType = models.CharField(max_length=20)
    superstrateManuf = models.CharField(max_length=20)
    substrateType = models.CharField(max_length=20)
    substrateManuf = models.CharField(max_length=20)
    frameType = models.CharField(max_length=20)
    frameAdhesive = models.CharField(max_length=20)
    encapsulantType = models.CharField(max_length=20)
    encapsulatManuf = models.CharField(max_length=20)
    junctionBoxType = models.CharField(max_length=20)
    junctionBoxManuf = models.CharField(max_length=20)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['prodName', 'cellTech', 'cellManuf', 
        'numCells', 'numCellsSeries', 'numSeriesStrings', 'numDiodes',
        'prodLength', 'prodWidth', 'superstrateType', 'superstrateManuf',
        'substrateType', 'substrateManuf', 'frameType', 'frameAdhesive', 
        'junctionBoxType', 'junctionBoxManuf']

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    officePhone = models.CharField(max_length=15)
    cellPhone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'firstName', 'middleName', 'lastName', 
        'address', 'officePhone', 'cellPhone', 'email', 'client']
    
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

class TestStandard(models.Model):
    testStandName = models.CharField(max_length=20)
    testStandDesc = models.CharField(max_length=255)
    testStandPubDate = models.CharField(max_length=10)

class TestStandardForm(ModelForm):
    class Meta:
        model = TestStandard
        fields = ['testStandName', 'testStandDesc', 'testStandPubDate']

class Certificate(models.Model):
    certID = models.CharField(max_length=8)
    user = models.ManyToManyField(User)
    reportNum = models.CharField(max_length=8)
    issueDate = models.CharField(max_length=10)
    testStandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelNum = models.ForeignKey(Product, on_delete=models.CASCADE)

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['certID', 'user', 'reportNum', 'issueDate', 
        'testStandard', 'location', 'modelNum']

class TestSequence(models.Model):
    sequenceName = models.CharField(max_length = 20)

class PerformanceData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence = models.ForeignKey(TestSequence, on_delete=models.CASCADE)
    maxSystemVolts = models.CharField(max_length=10)
    voc = models.CharField(max_length=10)
    isc = models.CharField(max_length=10)
    vmp = models.CharField(max_length=10)
    imp = models.CharField(max_length=10)
    pmp = models.CharField(max_length=10)
    ff = models.CharField(max_length=10)

class Service(models.Model):
    serviceID = models.CharField(max_length=8)
    description = models.CharField(max_length=255)
    isFiRequired = models.CharField(max_length=3)
    fiFrequency = models.CharField(max_length=10)
    standard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)   


