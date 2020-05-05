from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):

	condition_type=(
		('New','New'),
		('Used','Used')
	)
	"""docstring for Product"""
	name=models.CharField(max_length=100)
	#User from django
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	description=models.TextField(max_length=500)
	condition=models.CharField(max_length=100,choices=condition_type)

	category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
	brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)


	price=models.DecimalField(max_digits=10,decimal_places=5)
	image=models.ImageField(upload_to='main_product/',blank=True, null=True)

	date=models.DateTimeField(default=timezone.now)

	slug=models.SlugField(blank=True,null=True)

	def save(self,*args,**kwargs):
		if not self.slug and self.name:
			self.slug=slugify(self.name)
		super(Product,self).save(*args,**kwargs)


	def __str__(self):
		return self.name



class ProductImage(models.Model):
	"""docstring for Category"""
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='products/', blank=True, null=True)

	class Meta:
		verbose_name='Product Image'
		verbose_name_plural='Product Images'

	def __str__(self):
		return self.product.name



class Category(models.Model):
	"""docstring for Category"""
	category_name = models.CharField(max_length=50)
	image=models.ImageField(upload_to='category/',blank=True, null=True)

	slug=models.SlugField(blank=True,null=True)

	def save(self,*args,**kwargs):
		if not self.slug and self.category_name:
			self.slug=slugify(self.category_name)
		super(Category,self).save(*args,**kwargs)

	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'

	def __str__(self):
		return self.category_name



class Brand(models.Model):
	"""docstring for Category"""
	brand_name = models.CharField(max_length=50)

	class Meta:
		verbose_name='Brand'
		verbose_name_plural='Brands'

	def __str__(self):
		return self.brand_name
