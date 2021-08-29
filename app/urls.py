from django.urls import path

from .views import *

app_name = "main_app"

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('blog/<str:slug>/', DetailViews.as_view(), name='detailview'),
    path('categories/<str:slug>/', CategoriesView.as_view(), name='categories'),
    path('region/<str:slug>/', RegionsView.as_view(), name='regions'),
    path('hashtags/<str:slug>/', HashtegsView.as_view(), name='hashtags'),
]
