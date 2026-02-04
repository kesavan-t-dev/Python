from django.urls import path
from . import views

urlpatterns = [
    path('',views.urls_change, name = 'urls'),
    path('sample/',views.say_hellos, name = 'hello'),
    path('simple/', views.test_view, name = 'html-template'),
]