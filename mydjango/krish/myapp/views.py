from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    response=HttpResponse()
    response.write("<h1> My Garment com</h1>")
    response.write("<h2><i>the best garment shop in ammerpet hyderabad</i></h2>")
    response.write("<hr>")
    response.write('<a href="aboutus66">aboutus</a>')
    response.write('<br><a href="contactus99">contactus</a>')
    return response

def aboutus(request ,x):
    response=HttpResponse()
    response.write("<h1> This is about us page</h1>")
    response.write("<p> this is harikrishna naidu  my village name is tpasalavandlapalli gurramkondaMy Garment com</p>")
    response.write('u entered:%d'%x)
    return response

def contactus(request,n):
    response=HttpResponse()
    response.write("<h1> This is contact us page</h1>")
    response.write("<p> this is harikrishna naidu  my village name is tpasalavandlapalli gurramkondaMy Garment com</p>")
    response.write('u entered no :%d'%n)
    return response
