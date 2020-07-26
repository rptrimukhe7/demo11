from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Student
from .forms import StudentForm
# from .forms import StudentForm
# Create your views here.
def m1(request):
    return HttpResponse(" Hello Django")


def stu(request):
    data = Student.objects.all()
    return render(request,'demoapp/s.html',{'data':data})


def StuForm(request):
    form=StudentForm()
    #data=Student.objects.all()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'demoapp/form.html',{'form':form})




# data=Student.objects.all()
# for i in data:
#     print(i.first_name)
#     print(i.last_name)
#     print(i.roll_number)


# data= Student.objects.filter(id=1)
# data= Student.objects.filter(first_name='shekhar')

# print(data)