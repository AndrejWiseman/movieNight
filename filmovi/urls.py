from django.urls import path
from .views import filmovi, film_view

app_name = 'filmovi'

urlpatterns = [
    path('', filmovi, name='filmovi'),
    path('filmovi/<slug:slug>/', film_view, name='film_view'),

]