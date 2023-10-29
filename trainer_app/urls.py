from django.urls import path,include
from . import views


urlpatterns = [
    path('registration/', views.trainer_registration, name='trainer-registration'),  
    path('update/<int:trainer_id>/<str:lastname>/<str:firstname>/', views.trainer_update, name='trainer-update'), 
    path('trainer_list/', views.trainer_list, name='trainer-list'), 
    path('delete/<int:trainer_id>/', views.trainer_deletion, name='trainer-deletion'), 
]
