from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='homepage'),
    path('category', views.CategoryView, name='category'),
    path('about', views.AboutView, name='about'),
    path('latest-news', views.LatestNewsView, name='latest-news'),
]
