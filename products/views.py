from django.shortcuts import render
from django.views import ListView
from .models import Product

# Create your views here.

class ProductListView(ListView):
	queryset = Product.objects.all()


def productListView(request):
	context = {
	'object-list' : Product.objects.all()
	}
	return render(request,"product/productListView.html",context)


