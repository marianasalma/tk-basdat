from django.shortcuts import render

# Create your views here.
def form_kualifikasi(request):
    return render(request, "form_kualifikasi.html")

def pertanyaan_kualifikasi(request):
    return render(request, "pertanyaan_kualifikasi.html")

def pilih_stadium(request):
    return render(request, "pilih_stadium.html")

def pilih_event(request):
    return render(request, "pilih_event.html")

def pilih_kategori(request):
    return render(request, "pilih_kategori.html")

def daftar_atlet(request):
    return render(request, "daftar_atlet.html")

def list_atlet(request):
    return render(request, "list_atlet.html")

def daftar_sponsor(request):
    return render(request, "daftar_sponsor.html")

def enrolled_event(request):
    return render(request, "enrolled_event.html")

def list_event(request):
    return render(request, "list_event.html")