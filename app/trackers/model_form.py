from django.forms import ModelForm
from .models import Category

# Create the form class.
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]