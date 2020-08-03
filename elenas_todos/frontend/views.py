from django.shortcuts import render

# Create your views here.


def list(reques):
    return render(reques, 'frontend/list.html')
