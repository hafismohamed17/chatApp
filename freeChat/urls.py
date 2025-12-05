from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_page, name='home_page'),
    path('chat/',views.home,name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]