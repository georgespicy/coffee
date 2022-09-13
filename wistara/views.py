from django.shortcuts import redirect, render
from wistara.forms import ReservationForm, ReviewForm, SubcribeForm
from django.contrib.auth.decorators import login_required
from wistara.models import Menu, Menu_Category, Review
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
    reviews = Review.objects.all()
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
        'form':form,
        'reviews':reviews
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
    reservation = ReservationForm(request.POST)
    if request.method == 'POST':
        reservation = ReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('home')
        else:
            reservation = ReservationForm()
    else:
        reservation = ReservationForm()
# ============================================
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
        'reservation':reservation,
        'form':form
    }
    return render(request, 'wistara/reservation.html', context)

@login_required
def search(request):
    menu = Menu.object.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            menu = menu.filter(menu_name__icontains=keyword)
    context = {
        'menu':menu
    }
    return render(request, 'wistara/search.html', context)

@login_required
def addreview(request):
    if request.method == 'POST':
        review = ReviewForm(request.POST, request.FILES)
        if review.is_valid():
            review.save()
            print("Sent")
            return redirect('reviews')
        else:
            print("error")
            review = ReviewForm()
    else:
        review = ReviewForm()
    context = {
        'review':review
    }

    return render(request, 'wistara/review_form.html', context)