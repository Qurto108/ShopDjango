from django.urls import path
from .views import *

urlpatterns = [
    path('', PageHome.as_view(), name='urlHome'),
    path('search', SearchProduct.as_view(), name='urlSearch')
]
