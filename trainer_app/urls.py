from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/', views.regTrainerView, name='regTrainerView'),  
    path('update/<int:trainer_id>/<str:lastname>/<str:firstname>/', views.updTrainerView, name='updTrainerView'), 
    path('list/', views.listTrainerView, name='listTrainerView'), 
    path('delete/<int:trainer_id>/', views.delTrainerView, name='delTrainerView'), 
]