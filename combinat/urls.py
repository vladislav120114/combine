
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()

urlpatterns = [
    path('', views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('combinat/', views.index, name='home'),
    path('employee/', views.index_employee, name='employee'),
    path('location/', views.index_location, name='location'),
    path('product/', views.index_product, name='product'),
    path('weekly_prices_update/', views.index_weekly_prices_update, name='weekly_prices_update'),
    path('user/', views.index_user, name='user'),
    path('combine/', views.index_combine, name='combine'),
    path('prices/', views.index_prices, name='prices'),

    path("employee/add/", views.view_employee.add_employee, name="add_employee"),
    path("employee/del/", views.view_employee.del_employee, name="del_employee"),
    path("employee/up/", views.view_employee.update_employee, name="update_employee"),

    path("location/add/", views.view_location.add_location, name="add_location"),
    path("location/del/", views.view_location.del_location, name="del_location"),
    path("location/up/", views.view_location.update_location, name="update_location"),

    path("product/add/", views.view_product.add_product, name="add_product"),
    path("product/del/", views.view_product.del_product, name="del_product"),
    path("product/up/", views.view_product.update_product, name="update_product"),

    path("weekly_prices_update/add/", views.view_weekly_prices_update.add_weekly_prices_update, name="add_weekly_prices_update"),
    path("weekly_prices_update/del/", views.view_weekly_prices_update.del_weekly_prices_update, name="del_weekly_prices_update"),
    path("weekly_prices_update/up/", views.view_weekly_prices_update.update_weekly_prices_update, name="update_weekly_prices_update"),

    path("user/add/", views.view_user.add_user, name="add_user"),
    path("user/del/", views.view_user.del_user, name="del_user"),
    path("user/up/", views.view_user.update_user, name="update_user"),

    path("combine/add/", views.view_combine.add_combine, name="add_combine"),
    path("combine/del/", views.view_combine.del_combine, name="del_combine"),
    path("combine/up/", views.view_combine.update_combine, name="update_combine"),

    path("prices/add/", views.view_prices.add_prices, name="add_prices"),
    path("prices/del/", views.view_prices.del_prices, name="del_prices"),
    path("prices/up/", views.view_prices.update_prices, name="update_prices"),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]