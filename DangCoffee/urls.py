from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('infoapp.urls')),
]
=======
from recommend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('recommend1/', views.recommend1),
    path('recommend2/', include('recommend.urls')),
]
>>>>>>> 4b8ac64d3b3fc8879acfeb137cf51e972e96f2c5
