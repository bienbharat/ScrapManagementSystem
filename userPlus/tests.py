from django.test import TestCase
from typing import Set

# Create your tests here.
from .models import Company
from .models import Country


class CountryTestCase(TestCase):
    def setUp(self):
        Country.objects.create(Name="India")
        Country.objects.create(Name="UK")

    def test_country_has_india(self):
        c_india = Country.objects.get(Name="India")
        seen = set()
        seen.add(c_india)
        self.assertEqual(c_india.Name, 'India')
