from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        results = phones.order_by('name')
    elif sort == 'min_price':
        results = phones.order_by('price')
    elif sort == 'max_price':
        results = phones.order_by('-price')
    else:
        results = phones
    context = {
        'phones': results
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.get(slug=slug)
    context = {
        'phone': p
    }
    return render(request, template, context)
