from django.urls import path
from . import views


urlpatterns = [
    path('/', views.home, name = 'hospitalmain-home'),
    path('index/', views.index, name = 'hospitalmain-index'),
]