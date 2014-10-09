from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import attendance,office

def home(request):
	'''
	Homepage for attendance.
	Gives a search function to select students by course and semester
	-------------------------------------

	-------------------------------------
	
	'''
	data={}
	data['courses']=office.models.course.objects.all()
	data['semesters']=[1,2,3,4,5,6]
	return render(request,'attendance/home.html',data)

def student_id(request,studentid):
	'''
	for a student
	----------------------
	Provides attendance for student=student_attendance
	if student does not exist provides an error message
	----------------------
	'''
	data={}
	
	try:
		stud=office.models.student.objects.get(pk=studentid)
	except Exception as e:
		print e
		data['error']='Student Does not exist'
	else:
		data['student_attendance']=attendance.models.student_attendance.objects.filter(student=stud)
	return render(request,'attendance/student.html',data)
	
@require_http_methods(['POST'])
def get_student(request):
	'''
	meant for ajax requests.
	returns the list of students available for a combination of course and semester
	----------------------------------
	Returned in json format
	----------------------------------
	'''
	data={}
	
	try:
		course=office.models.course.objects.get(pk=request.POST['course'])
		semester=request.POST['semester']
	except Exception as e:
		print e
	else:
		try:
			students=office.models.student.objects.filter(course=course).filter(current_semester=semester)
			stu=[]
			for i in students:
				x={}
				x['name']=i.name
				x['id']=i.id
				stu.append(x)
			data['students']=stu
		except Exception as e:
			print e
	return HttpResponse(json.dumps(data),content_type='application/json')
