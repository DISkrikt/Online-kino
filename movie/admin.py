from django.contrib import admin
from .models import Movie
from .models import *

@admin.register(Movie) 
class MovieAdmin(admin.ModelAdmin):
    pass





@admin.register(MovieReview) 
class MovieReviewAdmin(admin.ModelAdmin):
    pass



@admin.register(Genre) 
class GenreAdmin(admin.ModelAdmin):
    pass



@admin.register(MoviePerson) 
class MoviePersonAdmin(admin.ModelAdmin):
    pass


# Register your models here.
