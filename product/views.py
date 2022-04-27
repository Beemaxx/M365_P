from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Vendor
from django.db.models import Q

# Create your views here.

class ProductListView(ListView):
    
    model = Product
    context_object_name = "product_list"
    template = "product_list.html"