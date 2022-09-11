from django.shortcuts import redirect, render
from wistara.forms import SubcribeForm

# Create your views here.

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

def menu(request):
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
    return render(request, 'wistara/menu.html', context)