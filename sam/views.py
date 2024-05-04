from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm,AddstudentForm,AddgoalForm
from .models import Student,Goal,Goal,Goal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    value= CreateUserForm()
    if request.method=='POST':
        value= CreateUserForm(request.POST)
        if value.is_valid():
            value.save()
            messages.success(request,'Account was Created Successfully...' , 'Now Click to Login...')
            return redirect('login')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = authenticate(request, password1=password1, password2=password2)
        if user is not None:
            login(request)
            return redirect('login')
        else:
            messages.info(request,'password should contains more than 8-Characters')
    return render(request,'sam/register.html',{'key':value})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            return redirect('student')
        else:
            messages.info(request,'Username or Password is Incorrect')
    content={}

    return render(request, 'sam/login.html',content)

def student(request):
    value=Student.objects.all()
    d={'key':value}
    return render(request, 'sam/student.html',d)

def addstudent(request):
    value=AddstudentForm
    if request.method=='POST':
        saveForm=AddstudentForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Student has been added...')
    d={'key':value}
    return render(request,'sam/addstudent.html',d)


def goal(request):
    value = Goal.objects.all()
    d = {'key': value}
    return render(request, 'sam/goal.html',d)


def addgoal(request):
    value=AddgoalForm
    if request.method=='POST':
        saveForm=AddgoalForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Goal has been added...')
    d={'key':value}
    return render(request,'sam/addgoal.html',d)

class detail(Goal):
    model = Goal
    context_object_name = "goals"

    def get_queryset(self):
        if self.kwargs['goalname']:
                # print("student_id :",self.kwargs['student_id'])
            return Goal.objects.filter ( goal_name=self.kwargs['goalname'] )
        return Goal.objects.all ()

def detail(request, goalname):
    goal_objects = Goal.objects.filter (goal_name=goalname )
    return render ( request, 'sam/detail.html',
                        context={'goalname': goalname, 'goals': goal_objects} )



def exam(request):
    value = Goal.objects.all()
    d = {'key': value}
    return render(request, 'sam/exam.html',d)


