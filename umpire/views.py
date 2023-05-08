from django.shortcuts import render

# Create your views here.


def show_perempat(request):
    return render(request, "perempat.html")


def show_semi(request):
    return render(request, "semi.html")


def show_final(request):
    return render(request, "final.html")


def show_hasil(request):
    return render(request, "hasil.html")
