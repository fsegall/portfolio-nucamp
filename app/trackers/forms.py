from django import forms


class CategoryNameForm(forms.Form):
    category_name = forms.CharField(label="Category name", max_length=100)