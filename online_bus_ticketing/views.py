from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is home page")


def login(request):
    return HttpResponse( )




def aboutUS(request):
    return HttpResponse("Welcome to Online Bus Ticketing")