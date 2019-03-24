from django.urls import path
from . import views

urlpatterns = [
    path('solutions/', views.SolutionListView.as_view(), name='lab.solutions'),
    path('solutions/detail/<int:pk>/', views.SolutionDetailView.as_view(), name='lab.solutions.detail'),
    path('solutions/update/<int:pk>/', views.SolutionUpdateView.as_view(), name='lab.solutions.update'),
    path('elements-solution/', views.ElementSolutionListView.as_view(), name='lab.elementssolution'),
    path('elements-solution/update/<int:pk>/', views.ElementSolutionUpdateView.as_view(), name='lab.elementssolution.update'),
    # path('groups/create', views.GroupCreateView.as_view(), name='greenhouse.groups.create'),
    # path('groups/update/<int:pk>/', views.GroupUpdateView.as_view(), name='greenhouse.groups.update'),
    # path('groups/detail/<int:pk>/', views.GroupDetailView.as_view(), name='greenhouse.groups.detail'),
]