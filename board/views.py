from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def signupfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'signup.html',{'error':'このユーザーはすでに使用されています'})
        except:
            user = User.objects.create_user(username2, "", password2)
            return render(request, 'signup.html', {'some':100})
    return render(request, 'signup.html', {'some':100})


@login_required
def listfunc(request):
    post_list=Post.objects.all()
    return render(request,'list.html',{'post_list':post_list})

def loginfunc(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        user = authenticate(request,username=username2, password=password2)
        if user is not None:
            login(request,user)
            return redirect('signup')
        else:
            return redirect('login')
    return render(request,'login.html')

    