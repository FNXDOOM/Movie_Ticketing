# Movie Reservation System

A web application for booking movie tickets online. Users can browse movies, view showtimes, and book tickets for their preferred shows.

## Features

- User registration and authentication
- Browse available movies
- View movie details and showtimes
- Book tickets for selected shows
- View booking history
- Admin panel for managing movies, shows, and bookings

## Technology Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### Installation

1. Clone the repository or download the source code

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL:
   - Create a database named `movie_reservation_db`
   - Update database settings in `movie_reservation/settings.py` if needed

5. Run migrations:
   ```
   cd movie_reservation
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at http://127.0.0.1:8000/

## Adding Movies via Admin Panel

Follow these steps to add movies and showtimes through the Django admin interface:

### Step 1: Access the Admin Panel
1. Start the Django server if it's not already running
2. Open your browser and go to http://127.0.0.1:8000/admin/
3. Log in with the superuser credentials you created during setup

### Step 2: Add a New Movie
1. In the admin dashboard, find the "Movies" section under "Booking"
2. Click on "Add" next to "Movies"
3. Fill in the movie details:
   - **Title**: The name of the movie
   - **Description**: A summary or synopsis of the movie
   - **Duration**: Length of the movie in minutes
   - **Genre**: Category of the movie (e.g., Action, Comedy, Drama)
   - **Release Date**: When the movie was released
   - **Poster**: Upload an image file for the movie poster (optional)
   - **Rating**: Movie rating on a scale (e.g., 8.5)
4. Click "Save" to add the movie

### Step 3: Add Showtimes for the Movie
1. Go back to the admin dashboard
2. Find the "Shows" section under "Booking"
3. Click on "Add" next to "Shows"
4. Fill in the show details:
   - **Movie**: Select the movie you just added from the dropdown
   - **Show Time**: Set the date and time for the show
   - **Available Seats**: Enter the total number of seats available
   - **Price**: Set the ticket price
   - **Screen**: Enter the screen number or name
5. Click "Save" to add the showtime

### Step 4: Add Multiple Showtimes (Optional)
- Repeat Step 3 to add multiple showtimes for the same movie
- You can add different showtimes, prices, or screens as needed

### Step 5: Verify the Added Content
1. Go to the main website (http://127.0.0.1:8000/)
2. Check if the newly added movie appears on the homepage
3. Click on the movie to see its details and available showtimes

## User Guide

- **Registration**: New users can register by clicking on the "Register" link
- **Login**: Existing users can log in using their credentials
- **Browsing Movies**: All available movies are displayed on the homepage
- **Movie Details**: Click on a movie to view its details and showtimes
- **Booking Tickets**: Select a showtime and specify the number of seats to book
- **My Bookings**: View your booking history and details

## Troubleshooting

- If images don't appear, make sure the media directory is properly configured
- For database connection issues, verify PostgreSQL is running and credentials are correct
- Check Django error logs for detailed error messages

### Project Url: https://github.com/FNXDOOM/Movie_Ticketing.git
