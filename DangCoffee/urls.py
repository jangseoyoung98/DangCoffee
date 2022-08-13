from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('infoapp.urls')),
]


import infoapp.views

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

