from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

# Create your views here.


def sayiDoldurma(request):

    return render(request, "pokust/sayi1.html")