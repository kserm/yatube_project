from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='main-view'),
    # path('groups/', views.groups_list),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('group_list/', views.group_list, name='group_list'),
]