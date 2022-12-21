import os
def handle_uploaded_file(f,foldername):  
    os.makedirs('projectworkapp/upload/'+foldername)
    with open('projectworkapp/upload/'+foldername+'/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 