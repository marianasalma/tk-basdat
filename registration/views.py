from django.shortcuts import render

# Create your views here.
def show_registration(request):
    return render(request, "registration.html")

def show_registration_atlet(request):
    return render(request, "registration_atlet.html")

def show_registration_pelatih(request):
    return render(request, "registration_pelatih.html")

def show_registration_umpire(request):
    return render(request, "registration_umpire.html")