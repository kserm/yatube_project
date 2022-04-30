# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main page')

def group_posts(requests, slug):
    return HttpResponse(f'Some group posts: '
                        f'{slug}')