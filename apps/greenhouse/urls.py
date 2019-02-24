from django.urls import path
from . import views

urlpatterns = [
    path('plant-types/', views.PlantTypeView.as_view(), name='greenhouse.plant-types'),

    path('plants/', views.PlantListView.as_view(), name='greenhouse.plants'),
    path('plants/create', views.PlantCreateView.as_view(), name='greenhouse.plants.create'),
    path('plants/detail/<int:pk>/', views.PlantDetailView.as_view(), name='greenhouse.plants.detail'),
    path('plants/update/<int:pk>/', views.PlantUpdateView.as_view(), name='greenhouse.plants.update'),

    path('controls/create/<int:pk>/', views.ControlCreateView.as_view(), name='greenhouse.controls.create'),
    path('controls/update/<int:pk>/', views.ControlUpdateView.as_view(), name='greenhouse.controls.update'),

    path('groups/', views.GroupListView.as_view(), name='greenhouse.groups'),
    path('groups/create', views.GroupCreateView.as_view(), name='greenhouse.groups.create'),
    path('groups/update/<int:pk>/', views.GroupUpdateView.as_view(), name='greenhouse.groups.update'),
    path('groups/detail/<int:pk>/', views.GroupDetailView.as_view(), name='greenhouse.groups.detail'),
]