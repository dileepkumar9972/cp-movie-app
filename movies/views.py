from django.shortcuts import render

# Create your views here.
from .models import Movie


def home_page(request):
    user_query = str(request.GET.get('query',''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_from_frontend = {"search_result":search_result}
    return render(request,'movies/movies_stuff.html',stuff_from_frontend)