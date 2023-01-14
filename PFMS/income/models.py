from django.db import models
from django.contrib.auth.models import User
import datetime
from BAM.models import Accounts



class Income_Category(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Income_Record(models.Model):
    account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Income_Category, null=True, on_delete=models.SET_NULL)
    details = models.TextField(null=True)
    amount = models.FloatField(null=False)
    date = models.DateField(null=False, default= datetime.date.today)
    time = models.TimeField(auto_now_add=True)
    
    # attachment = 

    def __str__(self):
        return f'{self.date}-{self.category}-{self.amount}'