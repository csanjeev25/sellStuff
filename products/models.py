from django.db import models
import random
import os

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

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10,decimal_places=2, default=3.99)
	image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

	def __str__(self):
		return self.title



