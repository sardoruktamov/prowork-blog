from django.urls import path
from .views import homeView, blogDetail


urlpatterns = [
    path('', homeView, name='home-view'),
    path('blogs/<int:id>', blogDetail, name='blog-detail')
]