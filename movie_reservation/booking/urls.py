from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('book/<int:show_id>/', views.book_ticket, name='book_ticket'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]