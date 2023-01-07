from django.shortcuts import render


def index(request):
    return render(request, "last_vacancies/index.html")
