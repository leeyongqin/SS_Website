from django.shortcuts import render

# Create your views here.


def website_index(request):
    return render(request, 'index.html', {})


def buy_page(request):
    return render(request, 'buy.html', {})


def archive_page(request):
    return render(request, 'archive.html', {})


def download_page(request):
    return render(request, 'download.html', {})