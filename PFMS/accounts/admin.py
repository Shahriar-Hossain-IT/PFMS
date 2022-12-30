from django.contrib import admin
from .models import Accounts, AccountTransaction
# Register your models here.

admin.site.register(Accounts)
admin.site.register(AccountTransaction)
