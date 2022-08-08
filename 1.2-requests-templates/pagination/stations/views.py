from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = []
    for row in reader:
        CONTENT.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    data = page.object_list
    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
