from django.urls import path
from login import views

urlpatterns = [
    path('create/', views.create),
    path('login/', views.login),
    path('validateuser/', views.validateuser),
    path('update/', views.update),

]

