from django.db import models

class employee(models.Model):
    id_user = models.ForeignKey('user', on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=45)
    objects = models.Manager()

class location(models.Model):
    region = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    objects = models.Manager()

class product(models.Model):
    product_name = models.CharField(max_length=45)
    product_sort = models.CharField(max_length=45)
    product_group = models.CharField(max_length=45)
    amount_of_product = models.CharField(max_length=45)
    id_combine = models.ForeignKey('combine', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class weekly_prices_update(models.Model):
    new_selling_price = models.CharField(max_length=45)
    new_purchase_price = models.CharField(max_length=45)
    id_prices = models.ForeignKey('prices', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class combine(models.Model):
    combine_name = models.CharField(max_length=45)
    combine_telephone_number = models.CharField(max_length=45)
    id_employee = models.ForeignKey('employee', on_delete=models.CASCADE, null=True)
    id_location = models.ForeignKey('location', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class user(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    birthday = models.CharField(max_length=45)
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    objects = models.Manager()

class prices(models.Model):
    selling_price = models.CharField(max_length=45)
    purchase_price = models.CharField(max_length=45)
    id_product = models.ForeignKey('product', on_delete=models.CASCADE, null=True)
    objects = models.Manager()











