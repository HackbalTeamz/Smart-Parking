from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.
class property(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	mapurl = models.CharField(max_length=500,default='')
	img1 = ResizedImageField(size=[500, 500],crop=['middle', 'center'],upload_to='property/pics', default='default.jpg')
	img2 = ResizedImageField(size=[500, 500],crop=['middle', 'center'],upload_to='property/pics', default='default.jpg')
	img3 = ResizedImageField(size=[500, 500],crop=['middle', 'center'],upload_to='property/pics', default='default.jpg')
	isactive = models.BooleanField(default=True)
	place = models.CharField(max_length=200,default='')
	district = models.CharField(max_length=200,default='')
	created_at = models.DateField(auto_now_add=True)
	owner = models.ForeignKey(User,default=None,on_delete=models.CASCADE)#for now to pass form validation,will remove later

	def __str__(self):
		return self.name

class pslot(models.Model):
	propertyid = models.ForeignKey(property,default=None,on_delete=models.CASCADE)
	isfw = models.BooleanField(default=False)
	istw = models.BooleanField(default=False)
	isavailable = models.BooleanField(default=True)
	isroofed = models.BooleanField(default=True)
	isfenced = models.BooleanField(default=True)

	def __str__(self):
		return self.propertyid.name

class userProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	state = models.CharField(max_length=200,default='')
	house = models.CharField(max_length=200,default='')
	town = models.CharField(max_length=200,default='')
	pincode = models.CharField(max_length=12,default='')
	phone = models.CharField(max_length=12,default='')
	isvendor = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
'''		
def check_product_stock(pid):
	product=products.objects.get(id=pid)
	if product.stock==0:
		product.isactive=False
		product.save()
		print("marked inactive")

class wishlist(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

class orderDetails(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	date = models.DateTimeField(auto_now_add=True)
	address = models.TextField()
	status = models.BooleanField(default=False)
	paymode = models.CharField(max_length=20,default=None)

class reviewDetails(models.Model):
	userid = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
	productid = models.ForeignKey(products,default=None,on_delete=models.CASCADE)
	stars = models.IntegerField(default=1)
	review = models.CharField(max_length=200,default='')	

'''