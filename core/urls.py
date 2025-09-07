from django.contrib import admin
from django.urls import path
from home.views import home, contact, about, success_page
from vege.views import (
    receipes, delete_receipe, update_receipe,
    login_page, register, logout_page
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
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
