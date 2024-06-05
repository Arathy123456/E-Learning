from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from learningapp.models import Userregistrations, profile, Classroom


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect(login1)


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        photo = request.POST['filename']

        # Perform basic validation
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.error(request, 'Username Exists! Try another Username...')
                return redirect('signup')
            else:
                if User.objects.filter(email=email):
                    return HttpResponse(request, 'Email Is Already Taken! Try Another One... ')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    #  reg = Userregistrations()
                    # reg.username = username
                    # reg.email = email
                    # reg.Password = password1
                    # reg.save()
                    # login(request, user)
                    profiles = Userregistrations(username=user, email=email, user_image=photo, Password=password1)
                    profiles.save()

                    messages.success(request, 'You have successfully Registered')
                    return redirect(login1)
        else:
            print('Password Did Not Matched!...')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login1(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('user')
        passwd = request.POST.get('pass')

        user = authenticate(username=name, password=passwd)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return redirect(home)
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect(login1)
    return render(request, 'login.html')


def profiles(request):
    context = {}
    user_id = request.user.id
    user_name = request.user.username
    user = User.objects.filter(id=user_id)
    prof = profile.objects.filter(user=request.user)
    user_details = Userregistrations.objects.get(username=request.user)

    user_image1=Userregistrations.objects.all()
   # print(user_image1    #  data=Userregistrations.objects.get(username=)


    details = Classroom.objects.all()
    if user_details and user_image1:

        return render(request, 'profile.html',
                      {'details': details, 'user_details': user_details, 'user': user, 'user_image1': user_image1})
    else:
        return render(request, 'home.html')


def videocall(request):
    user_name = request.user.username
    return render(request, 'WEB_UIKITS.html')


def logout1(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(login1)
