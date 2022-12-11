from django.contrib import admin
from django.urls import include, path

from .views import sayiDoldurma1, sayiDoldurma2, sayiDoldurma3

app_name = "pokust"

urlpatterns = [
    path('sayidoldurma1/', sayiDoldurma1, name="sayidoldurma1"),
    path('sayidoldurma2/', sayiDoldurma2, name="sayidoldurma2"),
    path('sayidoldurma3/', sayiDoldurma3, name="sayidoldurma4"),
]