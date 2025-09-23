from django.contrib import admin
from django.urls import path, include
from home.views import home, contact, about, success_page
from vege.views import (
    receipes, delete_receipe, update_receipe,
    login_page, register, logout_page, student_report, see_marks
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('receipes/', receipes, name="receipes"),
    path('delete-receipe/<int:id>/', delete_receipe, name="delete_receipe"),
    path('update-receipe/<int:id>/', update_receipe, name="update_receipe"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('register/', register, name="register"),
    path('success-page/', success_page, name="success_page"),
    path("students/", student_report, name="student_report"),
    path('see_marks/<str:student_id>/', see_marks, name="see_marks"),  # <str:student_id>
    path('admin/', admin.site.urls),
    path("", include("vege.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
