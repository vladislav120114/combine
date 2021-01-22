from django.test import TestCase
import unittest
from firstapp.models import employee, location, product, weekly_prices_update, user, combine, prices
# Create your tests here.
from django.urls import reverse
from firstapp.forms import Addemployee, Addlocation, Addproduct, Addweekly_prices_update, Adduser, Addcombine, Addprices

class employeeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        employee.objects.create(position='Оператор')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/employee/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('employee'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_employee.html')

class locationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        location.objects.create(region='Архангельский', city='Архангельск')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/location/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('location'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('location'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_location.html')

class productViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        product.objects.create(product_name='Свинная котлета', product_sort='Свинина', product_group='Котлеты', amount_of_product='150')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/product/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('product'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('product'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_product.html')

class weekly_prices_updateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        weekly_prices_update.objects.create(new_selling_price='2500', new_purchase_price='1000')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/weekly_prices_update/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('weekly_prices_update'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('weekly_prices_update'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_weekly_prices_update.html')

class userViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user.objects.create(firstname='Иван', lastname='Петров', birthday='19/07/1984', login='ivan_petrov', password='12345678')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/user/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_user.html')

class combineViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        combine.objects.create(combine_name='Мясокомбинат №1', combine_telephone_number='88005553535')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/combine/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('combine'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('combine'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_combine.html')

class pricesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        prices.objects.create(selling_price='2000', purchase_price='1500')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/prices/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('prices'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('prices'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firstapp/Template_prices.html')

class AnotherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user.objects.create(firstname='Иван', lastname='Петров', birthday='19/07/1984', login='ivan_petrov', password='12345678')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/combinat/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_view_url_exists_at_desired_location1(self): # существование url по адресу
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name1(self): # существование url по имени
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template1(self): # соответствие шаблону
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'great.html')