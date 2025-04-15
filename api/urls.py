from django.urls import path
from hello_app import views



urlpatterns = [
    path('index/', views.index,name='index'), 
    path('movies/', views.get_movies,name='get_movies'),
]
