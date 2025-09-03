from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('receipes/', receipes, name="receipes"),
    path('delete-receipe/<id>/', delete_receipe, name="delete_receipe"),  # fixed line
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('success-page/', success_page, name="success_page"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
