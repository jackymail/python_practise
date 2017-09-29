from django.http import HttpResponse
import random

def hello_world(request):
    return HttpResponse("hello world wide")


def root_page(request):
    return HttpResponse("Root Home Page")

def randome_number(request,max_rand=100):
    random_number = random.randrange(0,int(max_rand))
    msg = "Random number between 0 and %s :%d" % (max_rand,random_number)

    return  HttpResponse(msg)