from uuid import uuid4
from django.db import models
from django.utils import timezone
import pgtrigger 
# Create your models here.

class Customer(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid4,
         editable = False)
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'The customer name is: {self.full_name}.'

class Category(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    

class Balance(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid4,
         editable = False)
    current_balance = models.FloatField(default=0.0)
    previous_balance = models.FloatField(default=None)
    transaction_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    transaction_id = models.UUIDField(
         default = None,
         editable = True,
         unique=True,
         auto_created=False
         )

    def __str__(self):
        return f'Your current balance is {self.current_balance}'

class Income(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False)
    label = models.CharField(max_length=100)
    amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True) 
    created_at = models.DateTimeField()
    due_date = models.DateField(default=None)
    is_salary = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True) 

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name="track_balance_income",
                level=pgtrigger.Statement,
                when=pgtrigger.After,
                operation=pgtrigger.Insert,
                func=f"""INSERT INTO trackers_balance (current_balance, previous_balance, transaction_date, customer_id, transaction_id) VALUES (0.0, 0.0, now(), NEW.customer.id, NEW.income_id;""",
            )
        ]

    def __str__(self):
        return f'You have received {self.label} of: ${self.amount}'


class Expense(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False)
    label = models.CharField(max_length=100)
    amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True) 
    created_at = models.DateTimeField()
    due_date = models.DateField(default=None)
    is_bill = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name="track_balance_expense",
                level=pgtrigger.Statement,
                when=pgtrigger.After,
                operation=pgtrigger.Insert,
                func=f"""INSERT INTO trackers_balance (current_balance, previous_balance, transaction_date, customer_id, transaction_id) VALUES (0.0, 0.0, now(), NEW.customer.id, NEW.expense_id);""",
            )
        ]

    def __str__(self):
        return f'You have payed {self.label} of: ${self.amount}'
    



 