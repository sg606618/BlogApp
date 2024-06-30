from django.shortcuts import render


# Create your views here.
def blog(req):
    return render(req, 'category/blog.html')


def news(req):
    return render(req, 'category/news.html')
