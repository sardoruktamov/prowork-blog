from django.shortcuts import render, get_object_or_404
from .models import Regions, Category, Blog, Hashtags, PicturesFromTheBlog


# Create your views here.
def homeView(request):
    categories = Category.objects.all()
    regions = Regions.objects.all()
    blogs = Blog.objects.all()
    hashtegs = Hashtags.objects.all()
    

    context = {
        'categories':categories,
        'regions': regions,
        'blogs':blogs,
        'hashtegs':hashtegs,
    }
    return render(request, 'index.html', context)

def blogDetail(request, id):
    blogdetail = get_object_or_404(Blog, pk=id)
    categories = Category.objects.all()
    regions = Regions.objects.all()
    hashtegs = Hashtags.objects.all()
    picAdd = PicturesFromTheBlog.objects.filter(owner=blogdetail)
    print(picAdd,'++++++++++++++++++++++++++++++')

    context = {
        'categories':categories,
        'regions': regions,
        'hashtegs':hashtegs,
        'detail':blogdetail,
        'picAdd':picAdd
    } 
    return render(request, 'detail.html',context)