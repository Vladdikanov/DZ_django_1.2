from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_num = request.GET.get("page")
    with open(BUS_STATION_CSV, encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=",")
        CONTENT = list(file_reader)
        paginator = Paginator(CONTENT, 10)
        page = paginator.get_page(page_num)
        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
        # return HttpResponse(page)
