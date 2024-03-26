from django.http import HttpResponse

def index1(request):
    return HttpResponse("Hello world. Response for polls index1")

def index2(request):
    return HttpResponse("Response for index2 of polls")
