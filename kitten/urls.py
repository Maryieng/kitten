from django.urls import path
from rest_framework.routers import DefaultRouter

from kitten.views import (KittenCreateView, KittenListView, KittenRetrieveView, KittenUpdateView, KittenDestroyView,
                          BreedListView, RatingCreateView, RatingListView, )

app_name = 'kitten'


urlpatterns = [
    path('create/', KittenCreateView.as_view(), name='kitten_create'),
    path('', KittenListView.as_view(), name='kitten_list'),
    path('breed/', BreedListView.as_view(), name='breed_list'),
    path('view/<int:pk>/', KittenRetrieveView.as_view(), name='kitten_view'),
    path('update/<int:pk>/', KittenUpdateView.as_view(), name='kitten_update'),
    path('delete/<int:pk>/', KittenDestroyView.as_view(), name='kitten_delete'),
    path('kittens/<int:pk>/ratings/create/', RatingCreateView.as_view(), name='rating_create'),
    path('kittens/<int:pk>/ratings/', RatingListView.as_view(), name='rating_list'),]
