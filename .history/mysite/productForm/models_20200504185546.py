from django.db import models
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

###############################
#####Product from Dashboard####
###############################

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



