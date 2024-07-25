from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'board/signup.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
            return render(request, 'board/signup.html', {'some':100})
    return render(request, 'board/signup.html', {'some':100})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user = authenticate(request,username=username2, password=password2)
        if user is not None:
            login(request,user)
            return render(request,'board/signup.html')
        else:
            return render(request,'board/login.html')
    return render(request,'board/login.html')

def listfunc(request):
    return render(request,'board/list.html')

           
            
    