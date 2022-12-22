from django.db import models
import datetime
# Create your models here.


class Accounts(models.Model):
    account_name = models.CharField(max_length=60)
    account_no = models.CharField(max_length=20, null=True)
    custodial_name = models.CharField(max_length=20)
    account_balance = models.FloatField(null=False, default=0.0)
    opening_date= models.DateField(null=False, default= datetime.date.today)
    last_update_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.account_name


class Account_Transaction(models.Model):
    Transaction_Type = (
        ('C', 'Credit'),
        ('D', 'Debit'),
    )
    account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE)
    account_transaction_type = models.CharField(max_length=1, choices=Transaction_Type, null=False)
    ammount = models.FloatField(null=False)
    transaction_summary = models.TextField(null=True)
    date = models.DateField(null=False, default= datetime.date.today)

    def __str__(self):
        return self.account.account_name