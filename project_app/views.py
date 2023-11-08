from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
# from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import*
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')

def register(request):
    if request.method=='POST':

        First_Name=(request.POST['first_name'])
        Last_Name=(request.POST['last_name'])
        Email=(request.POST['email'])
        Mobile=(request.POST['mobile'])
        Password=(request.POST['password1'])
        Confirm_Password=(request.POST['password2'])

        # lower_email=Email.lower()

        print("Email value: ",Email)

        if Password != Confirm_Password:
            messages.warning(request,'Password & Confrim Password Not Match!')
            return render(request,'register.html')

        data={
            "First_Name":First_Name,
            "Last_Name":Last_Name,
            "Email":Email,
            "Mobile":Mobile,
            "Password":Password,
            "Confirm_Password":Confirm_Password,
        }

        a=RegisterForm(First_Name=First_Name,Last_Name=Last_Name,Email=Email,Mobile=Mobile,Password=Password,Confirm_Password=Confirm_Password)

        if RegisterForm.objects.filter(Email=Email).exists():

            messages.error(request,'Email Already Exist!! Try Login!')
            return render(request,'register.html')
        
        else:
            a.save()

            request.session['First_Name']=a.First_Name
            request.session['Last_Name']=a.Last_Name
            request.session['Email']=a.Email
            request.session['Password']=a.Password 
            request.session['id']=a.id

            request.session['is_logged']=True
            # messages.success(request,'Signup Success.')
            return render(request,'dashboard.html',{'name':a.First_Name})


def login_view(request):
      if request.method=="POST":
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        # lower_email=Email.lower()
        print("Email Login & Password:",Email,Password)

        try:
            print("email:",Email)
            context= RegisterForm.objects.get(Email=Email)
            print("Name: ",context.First_Name)

            if RegisterForm.objects.get(Email=Email):
                if (Password==context.Password):
                    request.session['First_Name']=context.First_Name
                    request.session['Last_Name']=context.Last_Name
                    request.session['Email']=context.Email
                    request.session['id']=context.id

                    request.session['is_logged']=True
                    # messages.success(request,'Sign In Success.')
                    return render(request,'dashboard.html',{'name':context.First_Name})
            
                else:
                    messages.error(request,'Invalid Password !')
                    return render(request,'login.html')
            
        except:

            messages.error(request,'Invalid Email !')
            return render(request,'login.html')


def dashboard(request):
    if request.session.has_key('is_logged'):
        return render(request, 'dashboard.html')
    messages.warning(request,'Please Login!')
    return render(request,'login.html')


def logout_view(request):
    request.session.flush()
    return render(request,'login.html')

def assigntask(request):
    userid=request.session.get("id")
    userlist=RegisterForm.objects.exclude(id=userid)
    return render(request,'assigntask.html',{'User':userlist})

def assignuser(request):
    Task_Name=request.POST["taskName"]
    TaskUserID=request.POST.get("userID")
    AssignUserID=request.session.get("id")
    TaskUserName=RegisterForm.objects.get(id=TaskUserID)
    AssignUserName=RegisterForm.objects.get(id=AssignUserID)
    taskdata={
        'Task_Name':Task_Name,
        'TaskUserID':TaskUserID,
        'AssignUserID':AssignUserID
    }

    data=ProjectTask(Task_Name=Task_Name,TaskUserID=TaskUserID,AssignUserID=AssignUserID,TaskUserName=TaskUserName.First_Name+" "+TaskUserName.Last_Name,AssignUserName=AssignUserName.First_Name+" "+AssignUserName.Last_Name)
    data.save()

    userlist=RegisterForm.objects.exclude(id=AssignUserID)

    messages.success(request,'Task Assigned Successfully!!!!')
    return render(request,'assigntask.html',{'User':userlist})

def mytask(request):
    userid=request.session.get('id')
    taskdata=ProjectTask.objects.filter(TaskUserID=userid)
    return render(request,'mytasklist.html',{'TaskData':taskdata})

def myassignlist(request):
    if request.session.has_key('is_logged'):
        userid=request.session.get("id")
        taskdata=ProjectTask.objects.filter(AssignUserID=userid)

        return render(request,'myassignlist.html',{'TaskData':taskdata})
    messages.warning(request,'Please Login!')
    return render(request,'login.html')

def userlist(request):
    userid=request.session.get("id")
    print("user id:",userid)
    userdata=RegisterForm.objects.exclude(id=userid)
    return render(request,'userlist.html',{'UserData':userdata})

def deletetask(request,action,id):
    if action=="deletetask":
        taskid=ProjectTask.objects.filter(id=id)
        data=taskid.delete()
        userid=request.session.get("id")
        taskdata=ProjectTask.objects.filter(AssignUserID=userid)
        return render(request,'myassignlist.html',{'TaskData':taskdata})
