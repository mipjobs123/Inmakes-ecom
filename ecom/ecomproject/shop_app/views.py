from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from shop_app.models import Category, Product
from django.core.paginator import Paginator, EmptyPage,InvalidPage
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug is not None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator1=Paginator(products_list,6)
    try:
        page1 = int(request.GET.get('page','1'))
    except:
        page1 = 1
    try:
        products = paginator1.page(page1)
    except (EmptyPage,InvalidPage):
        products = paginator1.page(paginator1.num_pages)

    return render(request,"category.html",{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
       raise e
    return render(request,'product.html',{'product':product})




