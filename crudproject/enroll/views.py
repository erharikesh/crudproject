from django.http.response import HttpResponseRedirect
from django.shortcuts import render 
from .forms import StudentRegistration   
from .models import User
 #Create your views here.
 #for show and add
def add_show(request):
 if request.method == 'POST':
     fm = StudentRegistration(request.POST) 
     if fm.is_valid():
         fm.save()
         fm = StudentRegistration()
 else:
        fm = StudentRegistration()
 stud = User.objects.all()
 return render(request,'enroll/addandshow.html', {'form':fm,'stu':stud})

#Udate and Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(request.POST,instance=pi)
  if fm.is_valid():
    fm.save()
 else:
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})


#for Delete
def delete_data(request,id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
    return HttpResponseRedirect('/')
    