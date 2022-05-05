# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context ={
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    # return HttpResponse(f'Some group posts: '
    #                     f'{slug}')
    template = 'posts/group_list.html'
     # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

def group_list(request):
    # return HttpResponse(f'Some group posts: '
    #                     f'{slug}')
    template = 'posts/group_list.html'
    posts = Post.objects.all()
    context ={
        'posts': posts,
    }
    return render(request, template, context)