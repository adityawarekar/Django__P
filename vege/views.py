from django.shortcuts import render
from .models import Receipe

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

    return render(request, "receipes.html")
