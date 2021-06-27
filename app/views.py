from django.shortcuts import render
from .models import Regions, Category, Blog, Hashtags, PicturesFromTheBlog


# Create your views here.
def homeView(request):
    categories = Category.objects.all()
    regions = Regions.objects.all()

    context = {
        'categories':categories,
        'regions': regions,
    }
    return render(request, 'index.html', context)