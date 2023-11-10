from django.urls import path
from .views import static_template_view, about_us_view, contact_us_view
from django.conf.urls.static import static
from django.conf import settings
from . import views

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

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),
    

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
