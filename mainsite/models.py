from django.db import models
from django import forms
from django.utils import timezone
import datetime
import random

class document(models.Model):
	'''
	Abstract class to contain the common things needed for notices etc.
	Basic document attributes.
	
	'''
	def __unicode__(self):
		return self.title
	title=models.CharField('The title of the document',max_length=50)
	associated_file=models.FileField('The associated file with this document',upload_to='document')
	alive=models.BooleanField('Is this document available for public use?',default=True)
	class Meta:
		abstract=True
class photo(models.Model):
	'''
	Abstract class to provide common attributes for photo data
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField('Name of the photo',max_length=40)
	associated_photo=models.ImageField('The associated image',upload_to='photos/hompage_slideshow/%Y/%m/%d')
	alive=models.BooleanField('Is this photo available for public use?',default=True)
	class Meta:
		abstract=True
	def thumbnail(self):
	        if self.associated_photo:
	        	addr=self.associated_photo.url
	        	addr.strip('/')
	        	addr='/'+addr
	                return u'<img src="'+addr+'" width=60 height=60 />'
	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True
	
class home_slideshow_photo(photo):
	'''
	Photos for homepage slideshow
	'''
	description=models.CharField('A description associated with the photo',max_length=50,blank=True,default='')
	
class notification(document):
	'''
	The notifications to be uploaded to the website.
	'''
	description=models.TextField('A description of the notification')
	publish_date=models.DateField(default=timezone.now())
	pinned=models.BooleanField('If this notification is to be permanently pinned on the homepage.',default=False)
	def recent(self):
		'''Checks if the record is one month old? Returns true if less than one month old.'''
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False
	recent.admin_order_field='publish_date'
	recent.boolean=True
	recent.short_description='Was published in last one month?'
		
class principal_desk(document):
	'''
	The articles to be uploaded under the principal's desk section.
	These are never deleted and hidden. They are always available.
	'''
	description=models.TextField('A description of the article')
	publish_date=models.DateField(default=timezone.now())
	def recent(self):
		'''Checks if the record is one month old? Returns true if less than one month old.'''
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False
	recent.admin_order_field='publish_date'
	recent.boolean=True
	recent.short_description='Was published in last one month?'

class admission_candidate(models.Model):
	'''
	model to handle admissions for the college.
	'''
	first_name=models.CharField(max_length=40)
	middle_name=models.CharField(max_length=40)
	last_name=models.CharField(max_length=40)
	
	picture=models.ImageField('Candidate photograph',upload_to='admission_photos/%Y/%m/%d')
	
	email=models.EmailField()
	#SUPER INSECURE PASSWORD FIELD--need to implement setpassword and check password
	#password= models.CharField(max_length=128, widget=forms.PasswordInput)	
	def thumbnail(self):
	        if self.picture:
      	        	addr=self.picture.url
	        	addr.strip('/')
	        	addr='/'+addr
	                return u'<img src="'+addr+'" width=60 height=60 />'

	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True

