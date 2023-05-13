from django.urls import path

from . import views

app_name = "trackers"

urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.CustomersListView.as_view(), name="customers"),
    path("customers/<str:pk>", views.CustomerSingleView.as_view(), name="customers_single"),
    path("transactions/", views.TransactionsListView, name="transactions"),
    path("transactions/incomes/<str:pk>", views.TransactionSingleView, name="transactions_income_single"),
    path("transactions/expenses/<str:pk>", views.TransactionSingleView, name="transactions_expense_single"),
    path("categories/", views.CategoriesListView.as_view(), name="categories"),
    path("categories/<str:pk>", views.CategorySingleView.as_view(), name="categories_single"),
    path("categories/thanks/", views.thanks, name="thanks")
]