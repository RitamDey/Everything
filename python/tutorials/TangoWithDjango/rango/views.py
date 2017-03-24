from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<title>Rango</title>\
                         <h1><center><i>Rango says\
                         \'Hey there patner\'</i></center></h1>\
                        <footer><a href='/rango/about/'>About Rango</a>")


def about(request):
    return render(request, "rango/about.html", {})
