from django.shortcuts import render,get_object_or_404, redirect
from .models import Store
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    site = Store.objects.first()
    return render(request, 'index.html', {'site': site})



def about(request):

    site = Store.objects.get(pk=2)

    return render(request, 'about.html', {'site':site})



def mylogin(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":

            user = authenticate(username=utxt, password=ptxt)

            if user != None:

                login(request, user)
                return redirect()

    return render(request, 'login.html')


def myregister(request):

    if request.method == 'POST':

        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            msg = "Your Pass Didn't Match"
            return render(request,'msgbox.html', {'msg':msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password1:

            if i > "0" and i < "9":
                count1 = 1
            if i > "A" and i < "Z":
                count2 = 1
            if i > 'a' and i < 'z':
                count3 = 1
            if i > "!" and i < "(":
                count4 = 1
        if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0:
            msg = "Your Pass Is Not Strong"
            return render(request, 'msgbox.html', {'msg':msg})

        if len(password1) < 8:
            msg = "Your Pass Most BE 8 Character"
            return render(request,'msgbox.html', {'msg':msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:

            user = User.objects.create_user(username=uname,email=email,password=password1)

    return render(request, 'login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')


def generic(request):


    return render(request, 'generic.html')



def elements(request):


   return render(request, 'elements.html')


def about_setting(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Requirded"
            return render(request, 'error.html', {'error':error})

        b = Store.objects.get(pk=2)
        b.abouttxt = txt
        b.save()

    about = Store.objects.get(pk=2).abouttxt


    return render(request, 'about_setting.html', {'about':about})


