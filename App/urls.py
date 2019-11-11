from django.urls import path

from .import views
app_name = 'App'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.my, name='login'),
    path('logout/', views.log, name='logout'),
    path('register/', views.register, name='register')
]
