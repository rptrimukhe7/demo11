from django.urls import path
from demoapp import views

urlpatterns = [
    path('hello/', views.m1),
    path('student/',views.stu),
    path('form/',views.StuForm),
]