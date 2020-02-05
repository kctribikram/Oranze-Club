from django.shortcuts import render,redirect
from app.forms import UserForm, GameForm, AdminForm, BookForm
from app.models import User, Games, Admin, Book
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

def signupadmin(request):
    if request.method=="POST":
        form=AdminForm(request.POST)
        form.save()
        return redirect('/')

    form=AdminForm()
    return render(request,"adminsignup.html",{'form':form})


def home(request):
    return render(request,"oranze.html")

def layout(request):
	return render(request,'layout.html')
	

def login(request):		
	return render(request,"login.html")	

def adminlogin(request):     
    return render(request,"adminlogin.html") 

def adminsignup(request):     
    return render(request,"adminsignup.html") 

@Authenticate.valid_admin
def admindetails(request):  
    admindetail=Admin.objects.all()   
    return render(request,"admindetails.html",{'admindetail':admindetail})  

       
@Authenticate.valid_admin
def bookdetails(request):  
    bookdetail=Book.objects.all()   
    return render(request,"bookdetails.html",{'bookdetail':bookdetail}) 

def entry(request):
    request.session['user_name']=request.POST['user_name']
    request.session['password']=request.POST['password']
    return redirect('/booking')


def adminentry(request):
    request.session['username']=request.POST['username']
    request.session['password']=request.POST['password']
    return redirect('/')
        

@Authenticate.valid_user
def booking(request):
    users=User.objects.all()
    return render(request,"booking.html",{'User':users})

def book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        form.save()
        return redirect('/home')

    form=BookForm()
    return render(request,"booking.html",{'form':form})    
			
#@Authenticate.valid_admin
def show(request):
	games=Games.objects.all()
	return render(request,"show.html",{'games':games})

@Authenticate.valid_admin
def players(request):
    limit=4
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:    
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*page    
        users=User.objects.raw("select * from user limit 4 offset %s",[offset])    
    else:
        users=User.objects.raw("select * from user limit 4 offset 0")  

    return render(request,"players.html",{'users':users,'page':page})	

def search(request):
    games=Games.objects.filter(name__contains=request.GET['srch']).values()
    return JsonResponse(list(games),safe=False)  	

@Authenticate.valid_admin
def create(request):
	if request.method=="POST":
		form=GameForm(request.POST)
		form.save()
		return redirect('/')

	form=GameForm()
	return render(request,"create.html",{'form':form})

def edit(request,game_id):
	game=Games.objects.get(game_id=game_id)
	return render(request,"edit.html",{'game':game})

def update(request,game_id):
	game=Games.objects.get(game_id=game_id)
	form=GameForm(request.POST,request.FILES,instance=game)
	form.save()
	return redirect('/')

def delete(request,game_id):
	game=Games.objects.get(game_id=game_id)
	game.delete()
	return redirect('/')


def logout(request):
    del request.session['user_name']
    del request.session['password']
    return redirect('/login')

