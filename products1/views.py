from django.shortcuts import render
from django.http import HttpResponse
from .models import dummproduts,Productinshop,Product
# Create your views here.

def index(request):
    tdummproduts = Productinshop.objects.all()
    return render(request,'index.html',{'products':tdummproduts})

def ProductId(request):
    productsID = Product.objects.all()
    val1 = request.POST["prId"]
    return render(request,'PRODUCT.html',{'result':val1,'products':productsID})