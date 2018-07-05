from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.http import Http404

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


def productDetailView(request,pk=None,*args,**kwargs):
	# # # print(args)
	# # # print(kwargs) 
	# try:
	# 	instance = Product.objects.get(pk=pk)
	# except Product.DoesNotExist:
	# 	# print("No Product Found")
	# 	raise Http404("No Product Found ")
	# except:
	# 	print("HUh")

	queryset = Product.objects.filter(pk=pk)
	if queryset.exists() and queryset.count() == 1:
		instance = queryset.first()
	else:
		raise Http404("No Product Found ")

	# instance = Product.objects.get(pk=pk)
	# instance = get_object_or_404(Product,pk=pk)
	context = {
	 'object' : instance
	 }
	return render(request,"products/detail.html",context)



