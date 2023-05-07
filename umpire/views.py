from django.shortcuts import render

# Create your views here.


def show_perempat(request):
    return render(request, "perempat.html")

def list_event(request):
    return render(request, "list_event.html")