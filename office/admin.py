from django.contrib import admin

from office.models import *


class course_type_inline(admin.TabularInline):
	'''inline addition for course_type'''
	model=course_type
	extra=1
	
class course_admin(admin.ModelAdmin):
	'''admin for course'''
	fieldsets=[
	(None,{'fields':['name']}),
	('Type of Course',{'fields':['type_of_course'],'classes':['collapse']}),
	]

	inlines=[course_type_inline]
	
	
#admin.site.register(course_type,course_type_admin)
#admin.site.register(course,course_admin)
