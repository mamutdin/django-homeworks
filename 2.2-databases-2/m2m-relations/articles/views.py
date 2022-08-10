from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all()
    context = {
        'object_list': object_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)


# def listing(request):
#     res = Article.objects.filter(tags__name='Космос')
#     print(res)
#     return HttpResponse(f'{res}')
