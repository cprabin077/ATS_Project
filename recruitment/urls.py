from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/create/', views.job_create, name='job_create'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/create/', views.candidate_create, name='candidate_create'),
]