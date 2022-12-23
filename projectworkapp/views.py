from django.shortcuts import render
from django.http import HttpResponse
from projectworkapp.function import handle_uploaded_file  
from projectworkapp.forms import SubmitForm  
#Authonication
from django.views import View
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def documentation(request):
    return render(request,"documentation.html")

def simulation(request):
    return render(request,"simulation.html")

def slide(request):
    return render(request,"slide.html")

def visualization(request):
    return render(request,"visualization.html")

def tests(request):  
    if request.method == 'POST': 
        s = SubmitForm(request.POST, request.FILES)
        if s.is_valid():  
            handle_uploaded_file(request.FILES['file'],request.POST['foldername'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        s = SubmitForm()  
        return render(request,"test.html",{'form':s})  


class Register(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'authentication/Register.html',locals())
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")  
        return render(request,'authentication/Register.html',locals()) 
