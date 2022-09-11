from django.urls import path
from account.views import register, login, user_logout


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', user_logout, name='logout'),
]
