from django.urls import path
from .views import login, logout, edit, register, verify

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
]
