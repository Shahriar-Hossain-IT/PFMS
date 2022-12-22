from django.db import models
import datetime
from accounts.models import Accounts



class Income_Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Income_Record(models.Model):
    date = models.DateField(null=False, default= datetime.date.today)
    time = models.TimeField(auto_now_add=True)
    category = models.ForeignKey(Income_Category, null=True, on_delete=models.SET_NULL)
    details = models.TextField(null=True)
    ammount = models.FloatField(null=False)
    account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE)
    # attachement = 

    def __str__(self):
        return f'{self.date}-{self.account.account_name}-{self.category}-{self.ammount}'
