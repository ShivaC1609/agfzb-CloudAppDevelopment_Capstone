
from .views import static_template_view, about_us_view, contact_us_view, login_view, logout_view, signup_view
from . import views
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import messages
from datetime import datetime
from django.urls import path
import logging
import json

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    path(route='static/', view=static_template_view, name='static_template'),
    # name the URL

    # path for about view
    path(route='about/', view=about_us_view, name='about_us'),

    # path for contact us view
    path(route='contact/', view=contact_us_view, name='contact_us'),

    # path for registration
    path(route='registration/', view=signup_view, name='signup'),


    # path for login
    path(route='login/', view=login_view, name='login'),

    # path for logout
    path(route='logout/', view=logout_view, name='logout_view'),

    
    

    # path for dealer reviews view
    path(route='', view=views.get_dealerships, name='index'),
    path(route='', view=views.home_view, name='index'),


    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
