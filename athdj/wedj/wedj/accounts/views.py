from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')


            else:
                user =User.objects.create(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect('/')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        
    else:
        return render(request,'register.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("check")
        print(username)
        print(password)

       
        #user = User.objects.get(username=username)
        # Check if the provided password matches the password stored in the database
        #if user.check(password):
           # print("correct")
            # Password is correct, return the user object
           # return user
        print("@@@@@@@@@@@@@@@@@@@@@@@@")
        try:
            user = User.objects.get(username=username)
            print(user)
            if user.password==password:
                print("Password is correct for the user:", username)
                print("okay")
            #login(request,user)
                return redirect('/we')
            else:
                messages.info(request,'Invalid credential')
            return redirect('/')
                       
        
           
                
        except:
            messages.info(request,'invalid credential')
            return redirect('/')

        
            
    return render(request,'login.html')
