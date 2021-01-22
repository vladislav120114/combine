from django.test import TestCase
import unittest
from firstapp.models import employee, location, product, weekly_prices_update, user, combine, prices

class employeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        employee.objects.create(position='Оператор')

    def test_position_label(self):
        Employee = employee.objects.get(id=1)
        field_label = Employee._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'position')

    def test_position_max_length(self):
        Employee = employee.objects.get(id=1)
        max_length = Employee._meta.get_field('position').max_length
        self.assertEquals(max_length, 45)

class locationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        location.objects.create(region='Архангельский', city='Архангельск')

    def test_region_label(self):
        Location = location.objects.get(id=1)
        field_label = Location._meta.get_field('region').verbose_name
        self.assertEquals(field_label,'region')

    def test_city_label(self):
        Location = location.objects.get(id=1)
        field_label = Location._meta.get_field('city').verbose_name
        self.assertEquals(field_label,'city')

    def test_region_max_length(self):
        Location = location.objects.get(id=1)
        max_length = Location._meta.get_field('region').max_length
        self.assertEquals(max_length, 45)

    def test_city_max_length(self):
        Location = location.objects.get(id=1)
        max_length = Location._meta.get_field('city').max_length
        self.assertEquals(max_length, 45)

class productModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        product.objects.create(product_name='Свинная котлета', product_sort='Свинина', product_group='Котлеты', amount_of_product='150')

    def test_product_name_label(self):
        Product = product.objects.get(id=1)
        field_label = Product._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label, 'product name')

    def test_product_sort_label(self):
        Product = product.objects.get(id=1)
        field_label = Product._meta.get_field('product_sort').verbose_name
        self.assertEquals(field_label, 'product sort')

    def test_product_group_label(self):
        Product = product.objects.get(id=1)
        field_label = Product._meta.get_field('product_group').verbose_name
        self.assertEquals(field_label, 'product group')

    def test_amount_of_product_label(self):
        Product = product.objects.get(id=1)
        field_label = Product._meta.get_field('amount_of_product').verbose_name
        self.assertEquals(field_label, 'amount of product')

    def test_product_name_max_length(self):
        Product = product.objects.get(id=1)
        max_length = Product._meta.get_field('product_name').max_length
        self.assertEquals(max_length, 45)

    def test_product_sort_max_length(self):
        Product = product.objects.get(id=1)
        max_length = Product._meta.get_field('product_sort').max_length
        self.assertEquals(max_length, 45)

    def test_product_group_max_length(self):
        Product = product.objects.get(id=1)
        max_length = Product._meta.get_field('product_group').max_length
        self.assertEquals(max_length, 45)

    def test_amount_of_product_max_length(self):
        Product = product.objects.get(id=1)
        max_length = Product._meta.get_field('amount_of_product').max_length
        self.assertEquals(max_length, 45)

class weekly_prices_updateModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        weekly_prices_update.objects.create(new_selling_price='2500', new_purchase_price='1000')

    def test_new_selling_price_label(self):
        Weekly_prices_update = weekly_prices_update.objects.get(id=1)
        field_label = Weekly_prices_update._meta.get_field('new_selling_price').verbose_name
        self.assertEquals(field_label, 'new selling price')

    def test_new_purchase_price_label(self):
        Weekly_prices_update = weekly_prices_update.objects.get(id=1)
        field_label = Weekly_prices_update._meta.get_field('new_purchase_price').verbose_name
        self.assertEquals(field_label, 'new purchase price')

    def test_new_selling_price_max_length(self):
        Weekly_prices_update = weekly_prices_update.objects.get(id=1)
        max_length = Weekly_prices_update._meta.get_field('new_selling_price').max_length
        self.assertEquals(max_length, 45)

    def test_new_purchase_price_max_length(self):
        Weekly_prices_update = weekly_prices_update.objects.get(id=1)
        max_length = Weekly_prices_update._meta.get_field('new_purchase_price').max_length
        self.assertEquals(max_length, 45)

class userModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user.objects.create(firstname='Иван', lastname='Петров', birthday='10/10/1990', login='ivan_petrov', password='********')

    def test_firstname_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('firstname').verbose_name
        self.assertEquals(field_label, 'firstname')

    def test_lastname_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('lastname').verbose_name
        self.assertEquals(field_label, 'lastname')

    def test_birthday_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label, 'birthday')

    def test_login_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('login').verbose_name
        self.assertEquals(field_label, 'login')

    def test_password_label(self):
        User = user.objects.get(id=1)
        field_label = User._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_firstname_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('firstname').max_length
        self.assertEquals(max_length, 45)

    def test_lastname_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('lastname').max_length
        self.assertEquals(max_length, 45)

    def test_birthday_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('birthday').max_length
        self.assertEquals(max_length, 45)

    def test_login_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('login').max_length
        self.assertEquals(max_length, 45)

    def test_password_max_length(self):
        User = user.objects.get(id=1)
        max_length = User._meta.get_field('password').max_length
        self.assertEquals(max_length, 45)

class combineModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        combine.objects.create(combine_name='Мясокомбинат №1', combine_telephone_number='88005553535')

    def test_combine_name_label(self):
        Combine = combine.objects.get(id=1)
        field_label = Combine._meta.get_field('combine_name').verbose_name
        self.assertEquals(field_label, 'combine name')

    def test_combine_telephone_number_label(self):
        Combine = combine.objects.get(id=1)
        field_label = Combine._meta.get_field('combine_telephone_number').verbose_name
        self.assertEquals(field_label, 'combine telephone number')

    def test_combine_name_max_length(self):
        Combine = combine.objects.get(id=1)
        max_length = Combine._meta.get_field('combine_name').max_length
        self.assertEquals(max_length, 45)

    def test_combine_telephone_number_max_length(self):
        Combine = combine.objects.get(id=1)
        max_length = Combine._meta.get_field('combine_telephone_number').max_length
        self.assertEquals(max_length, 45)

class pricesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        prices.objects.create(selling_price='2000', purchase_price='1000')

    def test_selling_price_label(self):
        Prices = prices.objects.get(id=1)
        field_label = Prices._meta.get_field('selling_price').verbose_name
        self.assertEquals(field_label, 'selling price')

    def test_purchase_price_label(self):
        Prices = prices.objects.get(id=1)
        field_label = Prices._meta.get_field('purchase_price').verbose_name
        self.assertEquals(field_label, 'purchase price')

    def test_selling_price_max_length(self):
        Prices = prices.objects.get(id=1)
        max_length = Prices._meta.get_field('selling_price').max_length
        self.assertEquals(max_length, 45)

    def test_purchase_price_max_length(self):
        Prices = prices.objects.get(id=1)
        max_length = Prices._meta.get_field('purchase_price').max_length
        self.assertEquals(max_length, 45)


