from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Receipe, Department, Student, SubjectMarks


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
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect('/login/')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required
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


@login_required
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


@login_required
def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('receipes')


def receipe_list(request):
    receipes = Receipe.objects.all().order_by("-receipe_view_count")
    return render(request, "receipe_list.html", {"receipes": receipes})


def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"department": departments})


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_report(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "students.html", {"page_obj": page_obj})


@login_required
def see_marks(request, student_id):
   
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)

  
    total_marks = queryset.aggregate(total=Sum('marks'))['total'] or 0

    
    all_totals = (
        SubjectMarks.objects.values('student__student_id__student_id')
        .annotate(total=Sum('marks'))
        .order_by('-total')
    )

    rank = None
    for idx, student in enumerate(all_totals, start=1):
        if student['student__student_id__student_id'] == student_id:
            rank = idx
            break

    return render(request, "see_marks.html", {
        "queryset": queryset,
        "total_marks": total_marks,
        "rank": rank,
    })
