from django.urls import path
from . import views

urlpatterns = [
    path('plants/', views.PlantListView.as_view(), name='greenhouse.plants'),
    path('plants/create', views.PlantCreateView.as_view(), name='greenhouse.plants.create'),
    path('plants/detail/<slug:slug>/', views.PlantDetailView.as_view(), name='greenhouse.plants.detail'),
    path('plants/update/<slug:slug>/', views.PlantUpdateView.as_view(), name='greenhouse.plants.update'),

    path('controls/create/<slug:slug>/', views.ControlCreateView.as_view(), name='greenhouse.controls.create'),
]