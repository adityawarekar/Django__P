from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Receipe



def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return redirect('/register/')

      
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)  # Hash password
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect('/login/')

    return render(request, 'register.html')


def login_page(request):
    return render(request, "login.html")



def receipes(request):
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("description")
        image = request.FILES.get("image")

        Receipe.objects.create(
            receipe_name=name,
            receipe_description=desc,
            receipe_image=image
        )
        return redirect('receipes')

    receipes = Receipe.objects.all()
    return render(request, "receipes.html", {"receipes": receipes})



def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        receipe.receipe_name = request.POST.get("name")
        receipe.receipe_description = request.POST.get("description")
        if request.FILES.get("image"):
            receipe.receipe_image = request.FILES["image"]
        receipe.save()
        return redirect('receipes')

    return render(request, "update_receipe.html", {"receipe": receipe})



def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('receipes')
