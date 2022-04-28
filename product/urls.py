from django.urls import path, include
from .views import *


urlpatterns = [ 
    path('', ProductListView.as_view(), name='product_list'),             #newAug17th
    path('<slug>/', ProductDetailView.as_view(), name='product_detail'),             #newAug17th
    #User Management
    path('accounts/', include('allauth.urls')),

]