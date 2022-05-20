from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import News, Tag


def page_list(set, request):
    paginator = Paginator(set, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


# Главная страница
def index(request):
    post_list = News.objects.all()
    page_obj = page_list(post_list, request)
    template = 'news/index.html'
    context = {
        'page_obj':page_obj,
    }
    return render(request, template, context)


# Страница со списком новостей по тегу
def news_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    news = News.objects.filter(tag=tag)
    page_obj = page_list(news, request)
    template = 'news/news_tag.html'
    context = {
        'page_obj': page_obj,
        'tag': tag,
    }
    return render(request, template, context)



def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    context = {
        'new': new,
    }
    return render(request, 'news/news_detail.html', context)