from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV
with open(BUS_STATION_CSV, encoding="utf-8") as file:
    file_reader = csv.reader(file, delimiter=",")
    print(list(file_reader)[0])