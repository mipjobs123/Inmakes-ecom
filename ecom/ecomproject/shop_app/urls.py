from . import views
from django.urls import path

app_name = 'shop_app'      #for name spacing

urlpatterns = [
    path('', views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail,name='prodCatdetail'),

]

