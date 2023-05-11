from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'The customer name is: {self.full_name}.'

class Category(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Income(models.Model):
    label = models.CharField(max_length=100)
    amount = models.FloatField()
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True) 
    created_at = models.DateTimeField()
    due_date = models.DateField(default=None)
    is_salary = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True) 
    def __str__(self):
        return f'You have received {self.label} of: ${self.amount}'

class Expense(models.Model):
    label = models.CharField(max_length=100)
    amount = models.FloatField()
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True) 
    created_at = models.DateTimeField()
    due_date = models.DateField(default=None)
    is_bill = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return f'You have payed {self.label} of: ${self.amount}'
    

class Balance(models.Model):
    current_balance = models.FloatField(default=0.0)
    previous_balance = models.FloatField(default=None)
    transaction_date = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE), # Decide if it stays
    income_id = models.ForeignKey(Income, on_delete=models.CASCADE, default=None)
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f'Your current balance is {self.current_balance}'



 