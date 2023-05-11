from django.shortcuts import render

# Create your views here.
from .models import Category, Customer
# from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from .forms import CategoryNameForm
from django.forms import modelformset_factory
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the trackers index.")

def thanks(request):
    return HttpResponse("Hello, world. You're have submitted a form.")

def transactions(request):
    return HttpResponse("Hello, world. You're at the trackers transactions page.")

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


def transactions_single(request, transaction_id):
    return HttpResponse("You're looking at transaction %s." % transaction_id)

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



