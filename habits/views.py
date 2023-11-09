from django.shortcuts import render
from django.http import HttpResponse

from .models import Habit
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchHabit')
    if searchTerm:
        habits = Habit.objects.filter(title__icontains=searchTerm)
    else:
        habits = Habit.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'habits':habits})

def about(request):
    return render(request, 'about.html')
    