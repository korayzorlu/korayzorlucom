from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

# Create your views here.


def sayiDoldurma1(request):

    return render(request, "pokust/sayi1.html")

def sayiDoldurma2(request):

    return render(request, "pokust/sayi2.html")

def sayiDoldurma3(request):

    return render(request, "pokust/sayi3.html")