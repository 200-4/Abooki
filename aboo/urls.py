from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('hire_me/', views.hire_me, name='hire_me'),
    path('learn_more/<int:service_id>/', views.learn_more, name='learn_more'),
    path('contact/', views.contact, name='contact'),
    #add more urls here
] 
