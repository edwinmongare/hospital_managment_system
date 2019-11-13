from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name = 'hospitalmain-index'),
    path('home/', views.home, name = 'hospitalmain-home'),
    path('queue/', views.queue, name = 'hospitalmain-queue'),
    
]