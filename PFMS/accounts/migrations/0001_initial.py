# Generated by Django 4.1.4 on 2022-12-22 18:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=60)),
                ('account_no', models.CharField(max_length=20, null=True)),
                ('custodial_name', models.CharField(max_length=20)),
                ('account_balance', models.FloatField(default=0.0)),
                ('opening_date', models.DateField(default=datetime.date.today)),
                ('last_update_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_transaction_type', models.CharField(choices=[('C', 'Credit'), ('D', 'Debit')], max_length=1)),
                ('ammount', models.FloatField()),
                ('transaction_summary', models.TextField(null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
    ]