from datetime import date
from django.shortcuts import render, HttpResponse
from news.models import Article, Reporter
# Create your views here.


def show(request):
    # print(Reporter.objects.all())
    # print(Article.objects.all())
    # r = Reporter(full_name='John Smith')
    # r.save()
    # print(r.id)

    # a.save()
    r = Article.reporter.full_name
    print(r)
    return HttpResponse("你好")