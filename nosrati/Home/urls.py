from django.urls import path

from .views import HomeView, Contact_us, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('about/', AboutView.as_view(), name='about-page'),
    path('contact_us/', Contact_us, name='contact-us'),
]
