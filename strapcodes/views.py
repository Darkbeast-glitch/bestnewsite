from django.shortcuts import render
from .models import News

# Create your views here.


def NewsIndex(request):
    #ohhh let's filter them by pub_date
    right_nav_news = News.objects.all()
    return render(request, 'pages/index.html', {'right_nav_news': right_nav_news})