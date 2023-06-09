from urllib import request
from django.shortcuts import render
from django.db.models import Sum

# Create your views here.
from .models import Category, Customer, Income, Expense, Balance
# from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from .forms import CategoryNameForm
from django.forms import modelformset_factory
from django.views import generic
from django.urls import reverse
import re

################### Placeholder Views
################### 

def index(request):
    return HttpResponse("Hello, world. You're are visiting the index page.")

def thanks(request):
    return HttpResponse("Hello, world. You're have submitted a form.")

################### Category
################### 

def categories(request):
    AuthorFormSet = modelformset_factory(Category, fields=["name"])
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # form = CategoryNameForm(request.POST)
        formset = AuthorFormSet(request.POST, request.FILES)
        # check whether it's valid:
        # if form.is_valid():
        if formset.is_valid():
            formset.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        # form = CategoryNameForm()
        category_list = Category.objects.order_by("created_at")[:5]
        context = {
        "category_list": category_list,
        "category_form": AuthorFormSet,
        }
        return render(request, "trackers/index.html", context)
    
    # template = loader.get_template("trackers/index.html")

    return render(request, "trackers/index.html", context)


# def categories_single(request, category_id):
#     # try:
#     #     category = Category.objects.get(pk=category_id)
#     # except Category.DoesNotExist:
#     #     raise Http404("Category does not exist")
#     category = get_object_or_404(Category, pk=category_id)
#     return render(request, "trackers/category_single.html", {"category": category})

#     return HttpResponse("You're looking at category %s." % category_id)

class CategoriesListView(generic.ListView):
    template_name = "trackers/index.html"
    # change variable in the trackers template index.html file to latest_category_list
    # context_object_name = "latest_category_list" 
    def get_queryset(self):
        """Return the last 2 published categories."""
        # return Category.objects.order_by("-created_at")[:2]
        return Category.objects.order_by("created_at")

class CategorySingleView(generic.DetailView):
    model = Category
    template_name = "trackers/category_single.html"

################### Customer
###################

class CustomersListView(generic.ListView):
    template_name = "trackers/customers.html"

    def get_queryset(self):
        try:
            return Customer.objects.order_by("created_at")
        except:
            return None
        
class CustomerSingleView(generic.DetailView):
    model = Customer
    template_name = "trackers/customer_single.html"
        
################### Balance
###################
        
def BalancesListView(request):
    template_name = "trackers/balances.html"

    tempDict = {}

    balances = Balance.objects.all()

    tempDict["customers_balance"] = balances
    
    return render(request,
                  template_name,
                  tempDict 
                  )

def BalancesClientListView(request):
    template_name = "trackers/balances.html"

    tempDict = {}

    customers_ids = []

    customers = Customer.objects.all()

    for customer in customers:
        customers_ids.append(customer.id)

    def get_incomes_expenses_per_customer(id_array):
        for id in id_array:
            full_name = Customer.objects.get(pk=id).full_name
            incomes = Income.objects.values_list('amount').filter(customer__id = id).aggregate(Sum('amount'))
            expenses = Expense.objects.values_list('amount').filter(customer__id = id).aggregate(Sum('amount'))
            tempDict[str(id)[:8]] = {'full_name': full_name, 'incomes': incomes, 'expenses': expenses}

    get_incomes_expenses_per_customer(customers_ids)

    def balance_per_customer():

        for customer in tempDict:

            print('**************************')

            print('Incomes Sum')
            print(tempDict[customer]['incomes'])
            print('Expenses Sum')
            print(tempDict[customer]['expenses'])

            print('**************************')

            print('Balance')

            print('**************************')

            tempDict[customer]['balance'] = tempDict[customer]['incomes']['amount__sum'] - tempDict[customer]['expenses']['amount__sum'] 

            print(tempDict[customer]['balance'])
    
    balance_per_customer()
        
    context = {}

    context["customers_balance"] = tempDict.values()
    
    return render(request,
                  template_name,
                  context 
                  )

################### Transaction
###################

def TransactionsListView(request):

    template_name = "trackers/transactions.html"

    context = {}

    context["income_list"] = Income.objects.all()
    context["expense_list"] = Expense.objects.all()

    return render(request,
                  template_name,
                  context 
                  )
        
def TransactionSingleView(request, pk):
    template_name = "trackers/transaction_single.html"

    customer_id = ""

    is_income = re.search("incomes", request.path)

    context = {}

    if is_income:
        income_item = Income.objects.get(pk=pk)
        context["income_item"] = income_item
        customer_id = income_item.customer_id
    else:
        expense_item = Expense.objects.get(pk=pk)
        context["expense_item"] = expense_item
        customer_id = expense_item.customer_id

    if customer_id:
        context["customer"] = Customer.objects.get(pk=customer_id)

    return render(request, template_name, context)




