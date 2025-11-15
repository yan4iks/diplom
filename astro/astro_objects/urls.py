from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:page>/', index, name='home_page'),
    path('stars/<slug:slug>/', views.star_detail, name='star-detail'),
    path('planets/<slug:slug>/', views.planet_detail, name='planet-detail'),
    path('planetary-systems/<int:pk>/planets/', views.planets_by_planetary_system, name='planets-by-system'),
    path('planetary-systems/<int:pk>/stars/', views.stars_by_planetary_system, name='stars-by-system'),
]