from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('new/', views.application_create, name='application_create'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
    path('<int:pk>/edit/', views.application_update, name='application_update'),
    path('<int:pk>/delete/', views.application_delete, name='application_delete'),
    path('about/', views.about, name='about'),
    path('sign-up/', views.sign_up, name='sign_up'),
]
