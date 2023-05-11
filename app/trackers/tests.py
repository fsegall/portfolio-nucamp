from django.test import TestCase
from django.urls import reverse
from .models import Category
from django.utils import timezone
import datetime


# Create your tests here.

class CategoryModelTest(TestCase):
    def test_was_saved_to_database_with_name(self):

        expected_name = "Category from test"
        other_name = "Not correct"

        new_category = Category(name = expected_name )
        new_category.save()

        retrieved_category_name = Category.objects.get(name=expected_name).name

        self.assertEqual(retrieved_category_name, expected_name)
    
class CategoryViewTest(TestCase):
    def test_categories_list_render(self):
        new_category1 = Category(name="Test Name 1")
        new_category2 = Category(name="Test Name 2")
        new_category1.save()
        new_category2.save()
        response = self.client.get(reverse("trackers:categories"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["category_list"], [new_category1, new_category2])

        
