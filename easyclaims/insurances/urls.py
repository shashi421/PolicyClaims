from django.urls import path
from insurances import views

urlpatterns = [
    path('createpolicy/', views.createpolicy),
    path('updatepolicy/', views.updatepolicy),
    path('getpolicy/', views.getpolicy),
    path('getallpolicy/', views.getallpolicy),

]
