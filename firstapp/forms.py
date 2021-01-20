from django import forms

class Addemployee(forms.Form):
    id_user = forms.CharField(label="ID пользователя", widget=forms.TextInput(attrs={"class": "myfield"}))
    position = forms.CharField(label="Должность", widget=forms.TextInput(attrs={"class": "myfield"}))

class Addlocation(forms.Form):
    region = forms.CharField(label="Регион",widget=forms.TextInput(attrs={"class":"myfield"}))
    city = forms.CharField(label="Город",widget=forms.TextInput(attrs={"class":"myfield"}))

class Addproduct(forms.Form):
    product_name = forms.CharField(label="Название продукта",widget=forms.TextInput(attrs={"class":"myfield"}))
    product_sort = forms.CharField(label="Сорт продукта",widget=forms.TextInput(attrs={"class":"myfield"}))
    product_group = forms.CharField(label="Группа продукта",widget=forms.TextInput(attrs={"class":"myfield"}))
    amount_of_product = forms.CharField(label="Кол-во продукта",widget=forms.TextInput(attrs={"class":"myfield"}))
    id_combine = forms.CharField(label="ID комбината производителя", widget=forms.TextInput(attrs={"class": "myfield"}))

class Addweekly_prices_update(forms.Form):
    new_selling_price = forms.CharField(label="Новая отпускная цена",widget=forms.TextInput(attrs={"class":"myfield"}))
    new_purchase_price = forms.CharField(label="Новая закупочная цена",widget=forms.TextInput(attrs={"class":"myfield"}))
    id_prices = forms.CharField(label="ID цен для замены", widget=forms.TextInput(attrs={"class": "myfield"}))

class Adduser(forms.Form):
    firstname = forms.CharField(label="Имя",widget=forms.TextInput(attrs={"class":"myfield"}))
    lastname = forms.CharField(label="Фамилия",widget=forms.TextInput(attrs={"class":"myfield"}))
    birthday = forms.CharField(label="Дата рождения",widget=forms.TextInput (attrs={"class":"myfield"}))
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "myfield"}))
    password = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={"class": "myfield"}))

class Addcombine(forms.Form):
    combine_name = forms.CharField(label="Название комбината",widget=forms.TextInput(attrs={"class":"myfield"}))
    combine_telephone_number = forms.CharField(label="Номер телефона комбината",widget=forms.TextInput(attrs={"class":"myfield"}))
    id_employee = forms.CharField(label="ID сотрудника комбината", widget=forms.TextInput(attrs={"class": "myfield"}))
    id_location = forms.CharField(label="ID расположения", widget=forms.TextInput(attrs={"class": "myfield"}))

class Addprices(forms.Form):
    selling_price = forms.CharField(label="Отпускная цена",widget=forms.TextInput(attrs={"class":"myfield"}))
    purchase_price = forms.CharField(label="Закупочная цена", widget=forms.TextInput(attrs={"class": "myfield"}))
    id_product = forms.CharField(label="ID продукта", widget=forms.TextInput(attrs={"class": "myfield"}))

