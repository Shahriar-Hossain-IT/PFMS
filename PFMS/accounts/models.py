from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Accounts(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=60, null=False)
    account_no = models.CharField(max_length=20, null=False)
    custodial_name = models.CharField(max_length=20, null=False)
    account_balance = models.FloatField(null=False, default=0.0)
    opening_date= models.DateField(null=False, default= datetime.date.today)
    last_update_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.account_name


class AccountTransaction(models.Model):
    Transaction_Type = (
        ('C', 'Credit'),
        ('D', 'Debit'),
        ('T', 'Transfer'),
    )
    account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE)
    account_transaction_type = models.CharField(max_length=1, choices=Transaction_Type, null=False)
    ammount = models.FloatField(null=False)
    transaction_summary = models.TextField(null=True)
    date = models.DateField(null=False, default= datetime.date.today)

    def __str__(self):
        return self.account.account_name


class InterAccountTransaction(models.Model):
    from_account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE, related_name ='from_account')
    to_account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE, related_name ='to_account')
    amount = models.FloatField(null=False)
    details = models.TextField(null=True)
    date = models.DateField(null=False, default= datetime.date.today)

    def __str__(self):
        return (f'{self.from_account.account_name} - {self.to_account.account_name} - {self.amount}')