from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView,self).get_context_data(*args,**kwargs)
		print(context)
		return context 



def productListView(request):
	context = {
	'object_list' : Product.objects.all()
	}
	return render(request,"products/list.html",context)

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context 



def productDetailView(request):
	context = {
	'object_list' : Product.objects.all()
	}
	return render(request,"products/detail.html",context)


