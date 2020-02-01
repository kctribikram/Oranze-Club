from django.shortcuts import render,redirect
from app.forms import UserForm, GameForm, AdminForm
from app.models import User, Game, Admin
from django.contrib import messages
from django.http import HttpResponse,JsonResponse

from app.authenticate import Authenticate


def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        user_name=request.POST['user_name']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password==repassword:
            if User.objects.filter(user_name=user_name).exists():
                messages.info(request,"username already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('/signup')
            else:
                userdata=User(fname=fname,lname=lname,email=email,number=number,user_name=user_name,
                                            password=password,repassword=repassword)
                userdata.save()
                print("user created")
                return redirect('/login')
        else:
            messages.info(request, "password didn't match")
            return redirect('/signup')
        return redirect('/login')
    else:
        return render(request,"signup.html")



def home(request):
    return render(request,"oranze.html")


	

def login(request):		
	return render(request,"login.html")	


def entry(request):
    request.session['user_name']=request.POST['user_name']
    request.session['password']=request.POST['password']
    return redirect('/booking')


        

@Authenticate.valid_user
def booking(request):
    users=User.objects.all()
    return render(request,"booking.html",{'User':users})
			
