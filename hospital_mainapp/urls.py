from django.urls import path
from . import views


urlpatterns = [
    path('/home', views.home, name = 'hospitalmain-home'),
    path('', views.index, name = 'hospitalmain-index'),
]