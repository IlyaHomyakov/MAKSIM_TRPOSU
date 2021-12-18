from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('film/<int:film_id>/', film, name='film')
]
