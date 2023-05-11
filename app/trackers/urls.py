from django.urls import path

from . import views

app_name = "trackers"

urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.CustomersListView.as_view(), name="customers"),
    path("customers/<int:pk>", views.CustomerSingleView.as_view(), name="customers_single"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/<int:transaction_id>", views.transactions_single, name="transactions_single"),
    path("categories/", views.CategoriesListView.as_view(), name="categories"),
    path("categories/<int:pk>", views.CategorySingleView.as_view(), name="categories_single"),
    path("categories/thanks/", views.thanks, name="thanks")
]