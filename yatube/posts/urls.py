from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('groups/', views.groups_list),
    path('group/<slug:slug>/', views.group_posts),
]