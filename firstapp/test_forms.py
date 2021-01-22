from django.test import TestCase
import unittest
from firstapp.forms import Addemployee, Addlocation, Addproduct, Addweekly_prices_update, Adduser, Addcombine, Addprices
# Create your tests here.

class AddemployeeFormTest(TestCase):

    def test_id_user_label(self):
        form = Addemployee()
        self.assertTrue(form.fields['id_user'].label == None or form.fields['id_user'].label == 'ID пользователя')

    def test_position_label(self):
        form = Addemployee()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_proverka(self):
        form = Addemployee(data={'id_user': 1, 'position': "Оператор"})
        self.assertTrue(form.is_valid())

class AddlocationFormTest(TestCase):

    def test_region_label(self):
        form = Addlocation()
        self.assertTrue(form.fields['region'].label == None or form.fields['region'].label == 'Регион')

    def test_city_label(self):
        form = Addlocation()
        self.assertTrue(form.fields['city'].label == None or form.fields['city'].label == 'Город')

    def test_proverka(self):
        form = Addlocation(data={'region': "Архангельский", 'city': "Архангельск"})
        self.assertTrue(form.is_valid())

class AddproductFormTest(TestCase):

    def test_product_name_label(self):
        form = Addproduct()
        self.assertTrue(form.fields['product_name'].label == None or form.fields['product_name'].label == 'Название продукта')

    def test_product_sort_label(self):
        form = Addproduct()
        self.assertTrue(form.fields['product_sort'].label == None or form.fields['product_sort'].label == 'Сорт продукта')

    def test_product_group_label(self):
        form = Addproduct()
        self.assertTrue(form.fields['product_group'].label == None or form.fields['product_group'].label == 'Группа продукта')

    def test_amount_of_product_label(self):
        form = Addproduct()
        self.assertTrue(form.fields['amount_of_product'].label == None or form.fields['amount_of_product'].label == 'Кол-во продукта')

    def test_id_combine_label(self):
        form = Addproduct()
        self.assertTrue(form.fields['id_combine'].label == None or form.fields['id_combine'].label == 'ID комбината производителя')

    def test_proverka(self):
        form = Addproduct(data={'product_name': "Свинная котлета", 'product_sort': "Свинина", 'product_group': "Котлеты", 'amount_of_product': "150", 'id_combine': 1})
        self.assertTrue(form.is_valid())

class Addweekly_prices_updateFormTest(TestCase):

    def test_new_selling_price_label(self):
        form = Addweekly_prices_update()
        self.assertTrue(form.fields['new_selling_price'].label == None or form.fields['new_selling_price'].label == 'Новая отпускная цена')

    def test_new_purchase_price_label(self):
        form = Addweekly_prices_update()
        self.assertTrue(form.fields['new_purchase_price'].label == None or form.fields['new_purchase_price'].label == 'Новая закупочная цена')

    def test_id_prices_label(self):
        form = Addweekly_prices_update()
        self.assertTrue(form.fields['id_prices'].label == None or form.fields['id_prices'].label == 'ID цен для замены')

    def test_proverka(self):
        form = Addweekly_prices_update(data={'new_selling_price': "2500", 'new_purchase_price': "1000", 'id_prices': 1})
        self.assertTrue(form.is_valid())

class AdduserFormTest(TestCase):

    def test_firstname_label(self):
        form = Adduser()
        self.assertTrue(form.fields['firstname'].label == None or form.fields['firstname'].label == 'Имя')

    def test_lastname_label(self):
        form = Adduser()
        self.assertTrue(form.fields['lastname'].label == None or form.fields['lastname'].label == 'Фамилия')

    def test_birthday_label(self):
        form = Adduser()
        self.assertTrue(form.fields['birthday'].label == None or form.fields['birthday'].label == 'Дата рождения')

    def test_login_label(self):
        form = Adduser()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'Логин')

    def test_password_label(self):
        form = Adduser()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль')

    def test_proverka(self):
        form = Adduser(data={'firstname': "Иван", 'lastname': "Петров", 'birthday': "19/07/1984", 'login': "ivan_petrov", 'password': "12345678"})
        self.assertTrue(form.is_valid())

class AddcombineFormTest(TestCase):

    def test_combine_name_label(self):
        form = Addcombine()
        self.assertTrue(form.fields['combine_name'].label == None or form.fields['combine_name'].label == 'Название комбината')

    def test_combine_telephone_number_label(self):
        form = Addcombine()
        self.assertTrue(form.fields['combine_telephone_number'].label == None or form.fields['combine_telephone_number'].label == 'Номер телефона комбината')

    def test_id_employee_label(self):
        form = Addcombine()
        self.assertTrue(form.fields['id_employee'].label == None or form.fields['id_employee'].label == 'ID сотрудника комбината')

    def test_id_location_label(self):
        form = Addcombine()
        self.assertTrue(form.fields['id_location'].label == None or form.fields['id_location'].label == 'ID расположения')

    def test_proverka(self):
        form = Addcombine(data={'combine_name': "Мясокомбинат №1", 'combine_telephone_number': "88005553535", 'id_employee': 1, 'id_location': 1})
        self.assertTrue(form.is_valid())

class AddpricesFormTest(TestCase):

    def test_selling_price_label(self):
        form = Addprices()
        self.assertTrue(form.fields['selling_price'].label == None or form.fields['selling_price'].label == 'Отпускная цена')

    def test_purchase_price_label(self):
        form = Addprices()
        self.assertTrue(form.fields['purchase_price'].label == None or form.fields['purchase_price'].label == 'Закупочная цена')

    def test_id_product_label(self):
        form = Addprices()
        self.assertTrue(form.fields['id_product'].label == None or form.fields['id_product'].label == 'ID продукта')

    def test_proverka(self):
        form = Addprices(data={'selling_price': "2000", 'purchase_price': "1000", 'id_product': 1})
        self.assertTrue(form.is_valid())