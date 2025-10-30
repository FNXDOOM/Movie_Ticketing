
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Movie, Show, Booking
from django.db import transaction

def home(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'movies': movies})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    shows = Show.objects.filter(movie=movie, available_seats__gt=0).order_by('show_time')
    return render(request, 'movie_detail.html', {'movie': movie, 'shows': shows})

@login_required
def book_ticket(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    
    if request.method == 'POST':
        seats = int(request.POST.get('seats', 1))
        
        if seats > show.available_seats:
            messages.error(request, 'Not enough seats available!')
            return redirect('movie_detail', movie_id=show.movie.id)
        
        with transaction.atomic():
            total_price = show.price * seats
            booking = Booking.objects.create(
                user=request.user,
                show=show,
                seats_booked=seats,
                total_price=total_price
            )
            show.available_seats -= seats
            show.save()
        
        messages.success(request, 'Booking confirmed!')
        return redirect('my_bookings')
    
    return render(request, 'book_ticket.html', {'show': show})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})