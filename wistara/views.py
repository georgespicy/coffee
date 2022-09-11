from django.shortcuts import redirect, render
from wistara.forms import SubcribeForm
from django.contrib.auth.decorators import login_required
from wistara.models import Menu, Menu_Category
# Create your views here.

@login_required
def home(request):
    form = SubcribeForm(request.POST)
    if request.method == 'POST':
        form = SubcribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SubcribeForm()
    else:
        form = SubcribeForm()
    context = {
        'form':form
    }
    return render(request, 'wistara/home.html', context)

@login_required
def about(request):
    form = SubcribeForm(request.POST)
    if request.method == 'POST':
        form = SubcribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SubcribeForm()
    else:
        form = SubcribeForm()
    context = {
        'form':form
    }
    return render(request, 'wistara/about.html', context)

@login_required
def reviews(request):
    form = SubcribeForm(request.POST)
    if request.method == 'POST':
        form = SubcribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SubcribeForm()
    else:
        form = SubcribeForm()
    context = {
        'form':form
    }
    return render(request, 'wistara/reviews.html', context)

# menu views
@login_required
def menu(request):
    menu = Menu_Category.objects.all()
    coffee = Menu.objects.all()
    form = SubcribeForm(request.POST)
    if request.method == 'POST':
        form = SubcribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SubcribeForm()
    else:
        form = SubcribeForm()
    context = {
        'coffee':coffee,
        'menu':menu,
        'form':form
    }
    return render(request, 'wistara/menu.html', context)

@login_required
def reservation(request):
    form = SubcribeForm(request.POST)
    if request.method == 'POST':
        form = SubcribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = SubcribeForm()
    else:
        form = SubcribeForm()
    context = {
        'form':form
    }
    return render(request, 'wistara/reservation.html', context)