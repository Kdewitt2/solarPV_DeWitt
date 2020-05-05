from django.db import models
from django.forms import ModelForm
from mysite.dashboard.models import Location, Product, TestStandard, User

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
    certID = models.CharField(max_length=8)
    user = models.ManyToManyField(User)
    reportNum = models.CharField(max_length=8)
    issueDate = models.CharField(max_length=10)
    testStandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelNum = models.ForeignKey(Product, on_delete=models.CASCADE)
