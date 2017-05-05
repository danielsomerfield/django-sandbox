from django.shortcuts import render


def index(request):
        return render(request, "d3/index.html")

