from django.shortcuts import render
from django.http import HttpResponse
from vege.seed import *

def home(request):
    seed_db(100)

    peoples = [
        {'name' : 'Aditya warekar', 'age' : 21},
        {'name' : 'Deep zade', 'age' : 25},
        {'name' : 'Ayush srode', 'age' : 17},
        {'name' : 'Aniket gawande', 'age' : 20},

    ]
    vegetables = ['Pumpkin', 'Tomato', 'Potatoe']
   
    return render(request , "index.html", context = {'peoples' : peoples, 'vegetables' : vegetables})
def about(request):
    return render(request , "home/about.html")                    

def contact(request):
    return render(request , "home/contact.html") 

def success_page(requests):
    return HttpResponse("<h1>Hey this is is a Success page</h1>")
