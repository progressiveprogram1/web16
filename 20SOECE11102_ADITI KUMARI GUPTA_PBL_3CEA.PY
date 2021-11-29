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
Hello everyone!!!
we all know to organize all the files manually is so boring and time taking task that's why we are going to use a python script that automatically organizes all the files.

First of all, we need to import the required modules i.e. import os and shutil module. These are inbuild Modules. So we don't need to install them and we need to create a variable called path which takes the input of the directory path we want to organize. And then create a variable called files which contains a list of files now we will write a for loop condition.
using for loop we traverse every file from files. Then we split the file name extension of files. We only need an extension name so we remove the. extension through slicing and then we need to write a statement if the extension directory already exists and then we move the file to that directory. In else statement we make a new directory then we move a file into it. Let run the program
copy path, enter the path. It's successfully executed, we can see files are correctly organized. Thats all about this code.
Thank you!!!


