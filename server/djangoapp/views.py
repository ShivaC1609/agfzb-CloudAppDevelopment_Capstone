from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def home_view(request):
    # Your existing logic for the home view
    return render(request, 'djangoapp/index.html')

def static_template_view(request):
    return render(request, 'djangoapp/static_template.html')


# Create an `about` view to render a static about page
# def about(request):
# ...
def about_us_view(request):
    return render(request, 'djangoapp/about.html')



# Create a `contact` view to return a static contact page
#def contact(request):
def contact_us_view(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_view(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('djangoapp:index') 
        else:
            messages.error(request, 'Invalid username or password.')

    # Your existing home view logic goes here
    # ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_view(request):
    logout(request)
    return redirect('djangoapp:index')  # Redirect to home after logout
# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('djangoapp:index')  # Redirect to the home page after signup
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = UserCreationForm()
    
    return render(request, 'djangoapp/registration.html', {'form': form})


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

