from django.contrib import admin

# Register your models here.
from .models import Balance, Income, Expense, Category, Customer

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Name", {"fields": ["name"]}),
        ("Date information", {"fields": ["created_at"]}),
    ]

admin.site.register(Category, CategoryAdmin)

admin.site.register([Balance, Income, Expense, Customer])