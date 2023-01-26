from django.shortcuts import render
from django.http import HttpResponse
from projectworkapp.function import handle_uploaded_file  
from projectworkapp.forms import SubmitForm  
#Authonication
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.core.mail import send_mail
from researchproject import settings,simulator
from django.contrib.auth.decorators import login_required

from .models import upload_file
from django.contrib.auth import views as User
#running simmulator

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def documentation(request):
    return render(request,"documentation.html")

@login_required(login_url='http://127.0.0.1:8000/login/')
def simulation(request):
        return render(request,"simulation.html")

@login_required(login_url='http://127.0.0.1:8000/login/')
def summary(request):
        mydict = {
            'submit': '10',
            'finish': '9',
            'error':'1'
            }
        return render(request,"accountsummary.html",{'id':mydict})

def slide(request):
    return render(request,"slide.html")

def visualization(request):
    return render(request,"visualization.html")
    
@login_required(login_url='http://127.0.0.1:8000/login/')
def tests(request):  
    if request.method == 'POST':
        #user_email = request.POST['email']
        filename = request.POST['foldername']
        currentuser = request.user
        s = SubmitForm(request.POST, request.FILES)
        if s.is_valid():  
            user_email = currentuser.email
            handle_uploaded_file(request.FILES['file'],request.POST['foldername'],currentuser.username)
            #return HttpResponse("File uploaded successfully")
            simulator.runsimulation()
            mail_message = f'The task  finished successfully.'\
                           f'You can view the results by visiting http://127.0.0.1:8000/result/{filename}/'
            send_mail('Your Result is Ready', mail_message, settings.EMAIL_HOST_USER, [user_email],fail_silently=False)
            return HttpResponse("File uploaded successfully Your Result is Ready Check Email")
    else:  
        s = SubmitForm()  
        return render(request,"test.html",{'form':s})

@login_required(login_url='http://127.0.0.1:8000/login/')
def result(request,id_user):
    currentuser = request.user
    user_name = currentuser.username
    return render(request,'result.html',{'id':user_name})


class Register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'authentication/Register.html',locals())
    def post(self,request):
        form = RegisterForm(request.POST)
        user_email= request.POST['email']
        user_username= request.POST['username']
        user_password1= request.POST['password1']
        if form.is_valid():
            form.save()
            mail_message=f'Your account Register successfully your Username is- {user_username} And Password is- {user_password1}'
            send_mail('Register account successfull',mail_message,settings.EMAIL_HOST_USER,[user_email],fail_silently=False)
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")  
        return render(request,'authentication/Register.html',locals()) 

@login_required(login_url='http://127.0.0.1:8000/login/')
def uploadfile(request):
    dict= {}
    if request.method == 'POST':
        form= SubmitForm(request.POST,request.FILES)
        if form.is_valid():
            currentuser = request.user
            user_email = currentuser.email
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            upload_file(file_name=name,my_file=the_files).save()
            dict["status"]= "{}Added successfully"
            simulator.runsimulation()
            mail_message = f'The task  finished successfully.'\
                           f'You can view the results by visiting http://127.0.0.1:8000/result/{name}/'
            send_mail('Your Result is Ready', mail_message, settings.EMAIL_HOST_USER, [user_email],fail_silently=False)
        else:
            dict["status"]= "{}Failed"
    else:
        dict = {
            'form':SubmitForm()
        }
    return render(request,'upload.html',dict)


@login_required(login_url='http://127.0.0.1:8000/login/')
def all(request):
    all_data = upload_file.objects.all()
    dict = {
        'data':all_data
    }
    return render(request,'res.html',dict) 