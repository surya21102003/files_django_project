from django.shortcuts import render,redirect
from .forms import MyFileForms
from .models import MyFileUpload
from django.contrib import messages
from django.urls import path
import os
# Create your views here.
def home(request):
    myform=MyFileForms
    mydata=MyFileUpload.objects.all()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'index.html',context)

    else:    
        context={'form':myform}
        return render(request,"index.html",context )


def uploadfile(request):
    if request.method=="POST":
        myform=MyFileForms(request.POST,request.FILES)
        if myform.is_valid:
            myfilename=request.POST.get('file_name')
            myfile=request.FILES.get('file')
            exists=MyFileUpload.objects.filter(myfile=myfile).exists()
            if exists:
                messages.error(request,'the file  is already exists...!!'% myfile)
            else:
                MyFileUpload.objects.create(file_name=myfilename,myfile=myfile).save()
                messages.success(request,"file upload successfully")
        return redirect('home')
    


def deletefile(request,id):
    mydata=MyFileUpload.objects.get(id=id)
    mydata.delete()
   # os.remove(mydata.myfile.path)
    messages.success(request,"file deleted successfully")
    return redirect('home')
    