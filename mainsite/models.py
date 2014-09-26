from django.db import models
from django.utils import timezone
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
	associated_photo=models.ImageField('The associated image',upload_to='photos/%Y/%m/%d')
	alive=models.BooleanField('Is this photo available for public use?',default=True)
	class Meta:
		abstract=True
	
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

