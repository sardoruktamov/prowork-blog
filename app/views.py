from django.shortcuts import render, get_object_or_404
from .models import Regions, Category, Blog, Hashtags, PicturesFromTheBlog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def homeView(request):
    categories = Category.objects.all()
    regions = Regions.objects.all()
    blogs = Blog.objects.all()
    hashtegs = Hashtags.objects.all()

    pgn = Paginator(blogs, 4)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'categories':categories,
        'regions': regions,
        'blogs':page,
        'hashtegs':hashtegs,
    }
    return render(request, 'index.html', context)

#postlarni batafsil ko`rish
def blogDetail(request, slug):
    blogdetail = get_object_or_404(Blog, slug=slug)
    categories = Category.objects.all()
    regions = Regions.objects.all()
    hashtegs = Hashtags.objects.all()
    picAdd = PicturesFromTheBlog.objects.filter(owner=blogdetail)
    for i in picAdd:
        print(i.image,'++++++++++++++++++++++++++++++')

    context = {
        'categories':categories,
        'regions': regions,
        'hashtegs':hashtegs,
        'detail':blogdetail,
        'picAdd':picAdd
    } 
    return render(request, 'detail.html',context)

#category bo`yicha filterlash
def category(request, slug):
    categorie = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=categorie)

    categories = Category.objects.all()
    regions = Regions.objects.all()
    hashtegs = Hashtags.objects.all()

    pgn = Paginator(blogs, 4)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'categories':categories,
        'regions': regions,
        'hashtegs':hashtegs,
        'blogs':page,
    } 
    
    return render(request, 'index.html', context)

#viloyatlar bo`yicha filterlash
def region(request, slug):
    region = get_object_or_404(Regions, slug=slug)
    blogs = Blog.objects.filter(region=region)

    categories = Category.objects.all()
    regions = Regions.objects.all()
    hashtegs = Hashtags.objects.all()

    pgn = Paginator(blogs, 4)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'categories':categories,
        'regions': regions,
        'hashtegs':hashtegs,
        'blogs':page,
    } 
    
    return render(request, 'index.html', context)

#hashteglar bo`yicha filterlash
def hashteg(request, slug):
    hashteg = get_object_or_404(Hashtags, slug=slug)
    blogs = Blog.objects.filter(hashtags=hashteg)

    categories = Category.objects.all()
    regions = Regions.objects.all()
    hashtegs = Hashtags.objects.all()

    pgn = Paginator(blogs, 4)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'categories':categories,
        'regions': regions,
        'hashtegs':hashtegs,
        'blogs':page,
    } 
    
    return render(request, 'index.html', context)