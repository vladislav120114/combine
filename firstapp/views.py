from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import employee, location, product, weekly_prices_update, user, combine, prices
from .forms import Addemployee, Addlocation, Addproduct, Addweekly_prices_update, Adduser, Addcombine, Addprices
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from firstapp import forms

def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")

def index_employee(request): #index_author
    form_employee = Addemployee()
    data = employee.objects.all()
    return render(request, "firstapp/Template_employee.html", {"form":form_employee, "data_show":data})

def index_location(request): #index_exhibition
    form_location = Addlocation()
    data = location.objects.all()
    return render(request, "firstapp/Template_location.html", {"form":form_location, "data_show":data})

def index_product(request):
    form_product = Addproduct()
    data = product.objects.all()
    return render(request, "firstapp/Template_product.html", {"form":form_product, "data_show":data})

def index_weekly_prices_update(request):
    form_weekly_prices_update = Addweekly_prices_update()
    data = weekly_prices_update.objects.all()
    return render(request, "firstapp/Template_weekly_prices_update.html", {"form":form_weekly_prices_update, "data_show":data})

def index_user(request):
    form_user = Adduser()
    data = user.objects.all()
    return render(request, "firstapp/Template_user.html", {"form":form_user, "data_show":data})

def index_combine(request):
    form_combine = Addcombine()
    data = combine.objects.all()
    return render(request, "firstapp/Template_combine.html", {"form":form_combine, "data_show":data})

def index_prices(request):
    form_prices = Addprices()
    data = prices.objects.all()
    return render(request, "firstapp/Template_prices.html", {"form":form_prices, "data_show":data})

#Определение view

class view_employee(View):
    def add_employee(request):
        if request.method == "POST":
            Employee = employee()
            Employee.id_user = user.objects.get(id=request.POST.get("id_user"))
            Employee.position = request.POST.get("position")
            Employee.save()
            return HttpResponseRedirect("/employee")

    def del_employee(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = employee.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/employee")

    def update_employee(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = employee.objects.get(id=q)
            que.id_user = user.objects.get(id=request.POST.get("id_user"))
            que.position = request.POST.get("position")
            que.save()
            return HttpResponseRedirect("/employee")

class view_location(View):
    def add_location(request):
        if request.method == "POST":
            Location = location()
            Location.region = request.POST.get("region")
            Location.city = request.POST.get("city")
            Location.save()
            return HttpResponseRedirect("/location")

    def del_location(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = location.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/location")

    def update_location(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = location.objects.get(id=q)
            que.region = request.POST.get("region")
            que.city = request.POST.get("city")
            que.save()
            return HttpResponseRedirect("/location")

class view_product(View):
    def add_product(request):
        if request.method == "POST":
            Product = product()
            Product.product_name = request.POST.get("product_name")
            Product.product_sort = request.POST.get("product_sort")
            Product.product_group = request.POST.get("product_group")
            Product.amount_of_product = request.POST.get("amount_of_product")
            Product.id_combine = combine.objects.get(id=request.POST.get("id_combine"))
            Product.save()
            return HttpResponseRedirect("/product")

    def del_product(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = product.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/product")

    def update_product(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = product.objects.get(id=q)
            que.product_name = request.POST.get("product_name")
            que.product_sort = request.POST.get("product_sort")
            que.product_group = request.POST.get("product_group")
            que.amount_of_product = request.POST.get("amount_of_product")
            que.id_combine = combine.objects.get(id=request.POST.get("id_combine"))
            que.save()
            return HttpResponseRedirect("/product")

class view_weekly_prices_update(View):
    def add_weekly_prices_update(request):
        if request.method == "POST":
            Weekly_prices_update = weekly_prices_update()
            Weekly_prices_update.new_selling_price = request.POST.get("new_selling_price")
            Weekly_prices_update.new_purchase_price = request.POST.get("new_purchase_price")
            Weekly_prices_update.id_prices = prices.objects.get(id=request.POST.get("id_prices"))
            Weekly_prices_update.save()
            return HttpResponseRedirect("/weekly_prices_update")

    def del_weekly_prices_update(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = weekly_prices_update.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/weekly_prices_update")

    def update_weekly_prices_update(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = weekly_prices_update.objects.get(id=q)
            que.new_selling_price = request.POST.get("new_selling_price")
            que.new_purchase_price = request.POST.get("new_purchase_price")
            que.id_prices = prices.objects.get(id=request.POST.get("id_prices"))
            que.save()
            return HttpResponseRedirect("/weekly_prices_update")

class view_combine(View):
    def add_combine(request):
        if request.method == "POST":
            Combine = combine()
            Combine.combine_name = request.POST.get("combine_name")
            Combine.combine_telephone_number = request.POST.get("combine_telephone_number")
            Combine.id_employee = employee.objects.get(id=request.POST.get("id_employee"))
            Combine.id_location = location.objects.get(id=request.POST.get("id_location"))
            Combine.save()
            return HttpResponseRedirect("/combine")

    def del_combine(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = combine.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/combine")

    def update_combine(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = combine.objects.get(id=q)
            que.combine_name = request.POST.get("combine_name")
            que.combine_telephone_number = request.POST.get("combine_telephone_number")
            que.id_employee = employee.objects.get(id=request.POST.get("id_employee"))
            que.id_location = location.objects.get(id=request.POST.get("id_location"))
            que.save()
            return HttpResponseRedirect("/combine")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            User = user()
            User.firstname = request.POST.get("firstname")
            User.lastname = request.POST.get("lastname")
            User.birthday = request.POST.get("birthday")
            User.login = request.POST.get("login")
            User.password = request.POST.get("password")
            User.save()
            return HttpResponseRedirect("/user")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = user.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/user")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = user.objects.get(id=q)
            que.firstname = request.POST.get("firstname")
            que.lastname = request.POST.get("lastname")
            que.birthday = request.POST.get("birthday")
            que.login = request.POST.get("login")
            que.password = request.POST.get("password")
            que.save()
            return HttpResponseRedirect("/user")

class view_prices(View):
    def add_prices(request):
        if request.method == "POST":
            Prices = prices()
            Prices.selling_price = request.POST.get("selling_price")
            Prices.purchase_price = request.POST.get("purchase_price")
            Prices.id_product = product.objects.get(id=request.POST.get("id_product"))
            Prices.save()
            return HttpResponseRedirect("/prices")

    def del_prices(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = prices.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/prices")

    def update_prices(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = prices.objects.get(id=q)
            que.selling_price = request.POST.get("selling_price")
            que.purchase_price = request.POST.get("purchase_price")
            que.id_product = product.objects.get(id=request.POST.get("id_product"))
            que.save()
            return HttpResponseRedirect("/prices")