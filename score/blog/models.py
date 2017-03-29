from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
#from ajaximage.fields import AjaxImageField 
# Create your models here.




'''
class Example(models.Model):
    thumbnail = AjaxImageField(upload_to='thumbnails',max_height=200, max_width=200, crop=True) 
	#def __str__(self):
	#	return str(self.thumbnail)
'''		
class Post(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	post = models.CharField(max_length=1000)
	date = models.DateTimeField(auto_now=True)
	is_draft = models.BooleanField(default = False)
	def __str__(self):
		return self.title


	
class Moreinfo(models.Model):
	
	user = models.ForeignKey(User)
	quote = models.CharField(max_length=150,blank=True,default=True)
	url = models.CharField(max_length=50,blank=True)
	about = models.CharField(max_length=150,blank=True)
	image = models.ImageField(upload_to='uploads/',blank=True)	

class PostView(models.Model):
	post = models.ForeignKey(Post)
	session = models.CharField(max_length=40)
	created = models.DateTimeField(auto_now=True)	
	user = models.CharField(max_length=30)

class T(models.Model):
	user =  models.ForeignKey(User)
	follows = models.ManyToManyField(User,related_name='follows')

class Tags(models.Model):
	tag = models.CharField(max_length=20)
	post = models.ForeignKey(Post) 
	def __str__(self):
		return self.tag
