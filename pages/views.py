from django.shortcuts import render
from strapcodes.models import News

# Create your views here.

def AboutView(request):
    context = {}
    return render(request, 'pages/about.html', context)

def CategoryView(request):
    context = {}
    return render(request, 'pages/category.html', context)

def IndexView(request):
    right_nav_news = News.objects.order_by('pub_date')[:4]
    trending_bottom_news = News.objects.order_by('pub_date')[:3]
    active_weekly_one = News.objects.filter(title__contains='weekly').order_by('-pub_date')[2]
    weekly_top_news = News.objects.filter(title__startswith='Weekly2')[:3]
    #actually they are all just 4 but should we have another post that's not what's new but starts also with Whats
    # I guess we have just 4 but were looking for 5 IndexOutOfRangeException
    whats_new_news = News.objects.filter(title__startswith='Whats').order_by('-pub_date')[:4]
    context = {
    'right_nav_news': right_nav_news, 
    'trending_bottom_news': trending_bottom_news,
     'active_weekly_one': active_weekly_one, 
     'weekly_top_news':weekly_top_news, 
     'whats_new_news': whats_new_news
     }
    return render(request, 'pages/index.html', context)

def LatestNewsView(request):
    context = {}
    return render(request, 'pages/latest-news.html', context)