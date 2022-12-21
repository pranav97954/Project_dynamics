from django import forms  
class SubmitForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email") 
    foldername =  forms.CharField(label="Enter folder name",max_length=50)  
    file      = forms.FileField() # for creating file input