from django.db import models
import random
import os
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.dispatch import receiver
from django.urls import reverse

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name,ext = os.path.splitext(base_name)
	return name,ext

def upload_image_path(instance,filename):
	#print(instance+filename)
	new_filename = random.randint(1,3910209312)
	name,ext = get_filename_ext(filename)
	final_file_name = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "products/{new_filename}/{final_file_name}".format(
		new_filename=new_filename,
		final_file_name=final_file_name)

class ProductQuerySet(models.query.QuerySet):
	def featured(self):
		return self.filter(featured=True,active=True)

	def active(self):
		return self.filter(featured=True,active=True)

class ProductManager(models.Manager):

	def get_queryset(self):
		return ProductQuerySet(self.model,using=self._db)

	def featured(self):
		return self.get_queryset().filter(featured=True)

	def all(self):
		return self.get_queryset().active()

	def features(self):
		return self.get_queryset().featured()

	def get_by_id(self,id): 
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True,blank=True)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10,decimal_places=2, default=3.99)
	image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	objects = ProductManager()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		#return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail",kwargs={"slug":self.slug})

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
    	instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)





