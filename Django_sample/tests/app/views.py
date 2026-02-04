from django.http import HttpResponse
import datetime 
def index(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)
    return HttpResponse(html)