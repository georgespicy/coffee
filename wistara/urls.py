from django.urls import path
from wistara.views import home, about, reviews, menu, reservation

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('reviews/', reviews, name='reviews'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation')
]