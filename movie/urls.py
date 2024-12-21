from django.urls import path 
from .views import *


urlpatterns = (
    path('', movielist, name='movielist'),
    path('movie_detail/<int:film_id>/', moviedetail, name='films'),
    path('add_movie_review/', add_movie_review, name='add_movie_review'),
    

)