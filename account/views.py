from django.shortcuts import redirect, render
from account.forms import UserRegistionForm
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form = UserRegistionForm(request.POST)
    if request.method == "POST":
        form = UserRegistionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegistionForm(request.POST)
    else:
        form = UserRegistionForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                return redirect('home')
        elif user is not None and not user.is_staff:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                return redirect('home')
        else:
            return redirect('home')
    context = {}
    return render(request, 'account/login.html', context)


@login_required
def user_logout(request):    
    logout(request)            
    return redirect('login')