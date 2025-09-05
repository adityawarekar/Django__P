from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe

# List + Add Recipe + Search
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

    # 🔎 Search functionality
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(receipe_name__icontains=search_query)

    context = {'receipes': queryset}
    return render(request, "receipes.html", context)


# Update Recipe
def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("description")
        image = request.FILES.get("image")

        receipe.receipe_name = name
        receipe.receipe_description = desc
        if image: 
            receipe.receipe_image = image
        receipe.save()

        return redirect('/receipes/')

    context = {"receipe": receipe}
    return render(request, "update_receipe.html", context)


# Delete Recipe
def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('/receipes/')
