
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    show_time = models.DateTimeField()
    available_seats = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    screen = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.movie.title} - {self.show_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.show.movie.title}"