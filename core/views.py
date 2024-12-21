from core.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        r_password = request.POST['repeat_password']
        if password != r_password:
            return render(request, 'core/signup.html', {
                'error':'Пароли не совпадают'
            })
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect('signin')
    return render(request, 'core/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(
            request, username=username, password=password
        )

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request,'core/signin.html', {
                'error':'Неверный логин или пароль'
            })
        
    return render(request, 'core/signin.html')

def signout(request):
    logout(request)
    return redirect("signin")

def profile(request):
    return render(request, 'core/profile.html')

