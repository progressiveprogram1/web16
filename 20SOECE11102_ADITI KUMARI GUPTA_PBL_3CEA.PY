#Name:Aditi Kumari Gupta
#Enrollment No:20SOECE11102
#Roll No:16
#Sec:3CEA
import os 
import shutil
path=input('enter path')
files=os.listdir(path)
for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension[1:]
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)