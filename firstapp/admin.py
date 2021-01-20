from django.contrib import admin
from .models import employee, location, product, weekly_prices_update, user, combine, prices

@admin.register(employee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'position')

@admin.register(location)
class locationAdmin(admin.ModelAdmin):
    list_display = ('region', 'city')

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_sort', 'product_group', 'amount_of_product', 'id_combine')

@admin.register(weekly_prices_update)
class weekly_prices_updateAdmin(admin.ModelAdmin):
    list_display = ('new_selling_price', 'new_purchase_price', 'id_prices')

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birthday', 'login', 'password')

@admin.register(combine)
class combineAdmin(admin.ModelAdmin):
    list_display = ('combine_name', 'combine_telephone_number', 'id_employee', 'id_location')

@admin.register(prices)
class pricesAdmin(admin.ModelAdmin):
    list_display = ('selling_price', 'purchase_price', 'id_product')
