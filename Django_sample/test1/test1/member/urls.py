from django.urls import path
from test1.member import views

urlpatterns = [
    path('members/', views.members, name='members'),
]