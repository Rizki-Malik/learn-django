from django.shortcuts import render, HttpResponse

# Create your view here


def home(request):
    return render(request, "home.html")