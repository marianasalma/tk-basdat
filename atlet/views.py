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