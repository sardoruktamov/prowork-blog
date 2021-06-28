from django.urls import path
from .views import homeView, blogDetail, category, region, hashteg


urlpatterns = [
    path('', homeView, name='home-view'),
    path('blogs/<slug:slug>', blogDetail, name='blog-detail'),
    path('category/<slug:slug>/', category, name="filter-category"),
    path('region/<slug:slug>/', region, name="filter-region"),
    path('hashtegs/<slug:slug>/', hashteg, name="filter-hashtegs"),
]