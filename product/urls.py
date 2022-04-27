from django.urls import path, include
from .views import *


urlpatterns = [ 
    path('', ProductListView.as_view(), name='book_list'),             #newAug17th


]