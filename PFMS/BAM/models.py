from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Accounts(models.Model):
    Account_Types = (
        ('Checking', 'Checking Account'),
        ('Savings', 'Savings Account '),
        ('BO', 'Beneficiary Owners Account'),
        ('FDR', 'Fixed Deposit Account'),
        ('RD/DPS', 'Recurring Deposit Account'),
        ('CDs', 'Certificate of Deposit Account'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=30, blank=False)
    account_no = models.IntegerField(blank=True)
    account_type = models.CharField(max_length=10, choices=Account_Types, null=False)
    custodial_name = models.CharField(max_length=20, null=False)
    account_balance = models.FloatField(null=False, default=0.0)
    opening_date= models.DateField(null=False, default= datetime.date.today)
    non_expenditure_account = models.BooleanField(null=False)
    last_update_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.account_name


class InterAccountTransaction(models.Model):
    from_account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE, related_name ='from_account')
    to_account = models.ForeignKey(Accounts, null=False, on_delete=models.CASCADE, related_name ='to_account')
    amount = models.FloatField(null=False, default=0.0)
    details = models.TextField(null=True)
    date = models.DateField(null=False, default= datetime.date.today)

    def __str__(self):
        return (f'{self.from_account.account_name} - {self.to_account.account_name} - {self.amount}')