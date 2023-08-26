from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import School
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , SchoolForm, TeacherRecordForm


# Create your views here.


def home(request):
    # if request.method == 'POST':

    return render(request, 'schSys/home.html', {})

@login_required
def teacherRecordForm(request):
    if request.user.is_authenticated:
        teacher_form = TeacherRecordForm
        if request.method == 'POST':
            teacher_form = TeacherRecordForm(request.POST, request.FILES)
            if teacher_form.is_valid():
                teacher_form.instance.user = request.user
                teacher_form.save()
                messages.success(request, 'Details Saved Successfully')
                return redirect ('teacher-record-form')
            else:
                messages.success(request, 'check your information provided well')
                # return redirect ('teacher-record-form')  
                return render(request, 'schRecords/teacherRecordForm.html', {'teacher_form':teacher_form})
                
        else:
            # messages.success(request, 'check the information provided well')
            # return redirect ('teacher-record-form')   
            return render(request, 'schRecords/teacherRecordForm.html', {'teacher_form':teacher_form})       
    else:
        messages.success(request, 'kindly sign in first')    
    return redirect('sign-in')

@login_required
def teacherProfile(request):
    
    return render(request, 'schRecords/teacherprofile.html', {})

@login_required
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
    if request.user.is_authenticated:
        school_form = SchoolForm
        if request.method == "POST":
            school_form = SchoolForm(request.POST)
            if school_form.is_valid:
                school_form.save()
                messages.success(request, 'School Registered Successfully')
                return redirect ('register-school')
            else:
                messages.success(request, 'Retry again')
                # return redirect ('register-school')
                return render (request, 'accounts/register-sch.html', {'school_form': school_form} )
        return render (request, 'accounts/register-sch.html', {'school_form': school_form} )
    else:
        messages.success(request, 'sign in first')
        return redirect ('sign-in')
        # return render (request, 'accounts/register-sch.html', {'school_form': school_form} )

        


def unsignedSearch(request):
    if request.method == 'POST':
        unsigned_query = request.POST['sch_query_unsigned']
        messages.success(request, "You searched for \"{}\" school, Sign in first for more information. Thank you.".format(unsigned_query))
        return redirect ('home')


def homeSearch(request):
    if request.user.is_authenticated:
    #     if request.method == "POST":
    #         schools = School.objects.get(id=pk)
    #         context = {'schools': schools}
    #         return render(request, 'schSys/home-search.html', context)
    #     return redirect ('home-search')
    # else:
    #     messages.success(request, "try signing in first")
    #     return render (request, 'schSys/home.html')
        
        signed_query = " "
        if request.method == "POST":
            signed_query = request.POST['sch_query'].capitalize()
            schools = School.objects.filter(name__contains=signed_query)
            # school_age = 2023
            context = {'schools': schools }
            return render (request, 'schSys/home_search.html', context)
        messages.success(request, "School \"{}\" is not registered.".format(signed_query))
        return redirect('home')
    else:
        messages.success(request, "sign in First")
        return redirect('sign-in')
        # return render (request, 'schSys/home_search.html')
    


