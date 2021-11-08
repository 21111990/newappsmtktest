from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('ProductId',views.ProductId,name='ProductId'),
    path('pdf_view',views.ViewPDF.as_view(),name='pdf_view'),
    path('nsdlesign',views.nsdlesign,name='nsdlesign')

]
