from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views import View


class PageHome(View):
    def get(self, request):
        return render(request, 'home.html')


class SearchProduct(View):
    def get(self, request):
        query = request.GET.get('q', '')
        
        search_product = Product.objects.filter(
            title__iregex = query
        ).values('title', 'price', 'photo')
        
        return JsonResponse({
            'succes': True,
            'query': query,
            'result': list(search_product),
            'count':len(search_product)
        }, status=200)
