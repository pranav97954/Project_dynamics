import os
from projectworkapp import UPLOAD_DIR

# def handle_uploaded_file(f,foldername):  
#     os.makedirs('projectworkapp/upload/'+foldername)
#     with open('projectworkapp/upload/'+foldername+'/'+f.name, 'wb+') as destination:  
#         for chunk in f.chunks():  
#             destination.write(chunk) 


def handle_uploaded_file(f, foldername, username):
    user_dir = os.path.join(UPLOAD_DIR, str(username))
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)

    task_dir = os.path.join(UPLOAD_DIR, str(username), str(foldername))
    if not os.path.exists(task_dir):
        os.mkdir(task_dir)

    with open(task_dir+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
