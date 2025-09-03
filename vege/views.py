from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('/receipes/')

    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, "receipes.html", context)


def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('/receipes/')
