from django.shortcuts import render

# Create your views here.


def show_perempat(request):
    return render(request, "perempat.html")
