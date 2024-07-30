from django.urls import path
from users import views

app_name='users'
urlpatterns = [
    path('register/',views.register,name='reg'),
    path('profile/',views.profile,name='profile'),
]