"""
URL configuration for project1 project.
"""
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("sample/",include("test1.urls"))
]
