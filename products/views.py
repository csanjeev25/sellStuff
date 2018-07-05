from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.http import Http404

# Create your views here.

class ProductListView(ListView):
	# queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context 

	def get_queryset(self,*args,**kwargs):
		request = self.request
		print(Product.objects.all())
		return Product.objects.all() 

class ProductFeaturedListView(ListView):
	# queryset = Product.objects.all(featured=True)
	template_name = "products/featured_list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context 

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.featured() 

class ProductFeaturedDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/featured_detail.html"

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.featured() 



def productListView(request):
	context = {
	'object_list' : Product.objects.all()
	}
	return render(request,"products/list.html",context)

class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context 

	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None :
			raise Http404("No Product Found ")
		return instance

	# def get_query_set(self,*args,**kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Product.objects.filter(pk)

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		print(slug)
		#instance = get_object_or_404(Product,slug=slug,active=True)
		try:
			instance = Product.objects.get(slug=slug,active=True)
		except Product.DoesNotExist:
			raise Http404("No Product Found Bitch!!!")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug,active=True)
			instance = qs.first()
		except:
			raise Http404("Valar Morghulis")
		# if instance is None :
		# 	raise Http404("No Product Found ")
		return instance



def productDetailView(request,pk=None,*args,**kwargs):
	# # # print(args)
	# # # print(kwargs) 
	# try:
	# 	instance = Product.objects.get(pk=pk,featured=False,featured=True)
	# except Product.DoesNotExist:
	# 	# print("No Product Found")
	# 	raise Http404("No Product Found ")
	# except:
	# 	print("HUh")

	instance = Product.objects.get_by_id(pk) 
	# print(instance)

	# queryset = Product.objects.filter(pk=pk)
	# if queryset.exists() and queryset.count() == 1:
	# 	instance = queryset.first()
	# else:
	# 	raise Http404("No Product Found ")

	# instance = Product.objects.get(pk=pk)
	# instance = get_object_or_404(Product,pk=pk)
	if instance is None :
		raise Http404("No Product Found ")
	context = {
	 'object' : instance
	 }
	return render(request,"products/detail.html",context)



