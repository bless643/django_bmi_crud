from django.urls import path
from .import views

urlpatterns = [
    path('create/', views.create, name='createpage'),
    path('', views.read, name='readpage'),
    path('delete/<int:pk>', views.delete, name='deletepage'),
    path('update/<int:pk>', views.update, name='updatepage')



]
