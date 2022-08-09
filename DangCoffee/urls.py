from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from recommend import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('recommend1/', views.recommend1),
    path('recommend2/', include('recommend.urls')),

    path('login/', accounts_views.login, name="login"),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),

]
