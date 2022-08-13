from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('infoapp.urls')),
]
=======
=======

import infoapp.views
>>>>>>> e271b359f8ee51e3ea8ab334f0ccb5e2ffda04f9
from recommend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', infoapp.views.productlist),
    path('info/', include('infoapp.urls')),
    path('', views.home),
    path('recommend1/', views.recommend1),
    path('recommend2/', include('recommend.urls')),
    path('beverage/', include('beverage.urls'))
]
<<<<<<< HEAD
>>>>>>> 4b8ac64d3b3fc8879acfeb137cf51e972e96f2c5
=======
>>>>>>> e271b359f8ee51e3ea8ab334f0ccb5e2ffda04f9
