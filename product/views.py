from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Vendor
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

class ProductListView(ListView):
    
    model = Product
    context_object_name = "product_list"
    template = "product_list.html"
    
    
class ProductDetailView(DetailView):
    
    model = Product
    template = "product_detail.html"
    queryset = Product.objects.all()
    
    def listing(request):
        queryset = Product.objects.all()

        paginator = Paginator(queryset, 9) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "product_detail.html", {'page_obj': page_obj})
        
   
    