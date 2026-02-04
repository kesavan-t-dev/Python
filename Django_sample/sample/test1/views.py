from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("hello...")
def say_hellos(request):
    return HttpResponse("hello.s..")


def urls_change(request):
    return HttpResponse("url changed")

def test_view(request):
    return render(request, "index.html")


# def simple_view(request):
#     context = {"data": "template is working"}
#     return render(request, "Sample.html", context)