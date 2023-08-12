from django.shortcuts import render, redirect
from .models import School
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.


def home(request):
    # if request.method == 'POST':

    return render(request, 'schSys/home.html', {})

def teacherRecordForm(request):
    return render(request, 'schRecords/teacherRecordForm.html', {})

def teacherProfile(request):
    return render(request, 'schRecords/teacherprofile.html', {})

def teacherList(request):
    return render(request, 'schRecords/teacherList.html', {})


def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Signed in successfully!")
            return redirect('home')
        else:
            messages.success(request, "Error, check credentials and try again.")
            return render (request, 'accounts/signIn.html', {})
    return render (request, 'accounts/signIn.html', {})

def signOut(request):
    logout(request)
    messages.success(request, 'Your are signed out.')
    return redirect ('sign-in')
            


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Succesfully!")
            return redirect('sign-in')
    else:
        form = RegisterForm()
        context = {'form': form}
        return render (request, 'accounts/register.html', context )
    context = {'form': form}
    return render (request, 'accounts/register.html', context )


def registerSchool(request):
    return render (request, 'accounts/register-sch.html', {} )


def unsignedSearch(request):
    if request.method == 'POST':
        unsigned_query = request.POST['sch_query_unsigned']
        messages.success(request, "You searched for \"{}\" school, Sign in first for more information. Thank you.".format(unsigned_query))
        return redirect ('home')

    
def homeSearch(request):
    if request.method == "POST":
        schools = " "
        signed_query = request.POST['sch_query']
        schools = School.objects.filter(name__contains=signed_query)
        school_age = 2023
        # context = {'schools': schools }
        return render (request, 'schSys/home_search.html',{'schools': schools, 'school_age': school_age })
    else:
       
        
        messages.success(request, " School \'{}\' is not registered.".format(signed_query_wrong))
        return redirect('home-search')
    


