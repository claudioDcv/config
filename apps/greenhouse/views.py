from django.urls import reverse
from django.utils import timezone
from datetime import datetime
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from .models import Plant, Control
from .forms import PlantForm, ControlForm

class PlantListView(LoginRequiredMixin, ListView):
    model = Plant

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    success_url = '/greenhouse/plants/'
    form_class = PlantForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return FormMixin.form_valid(self, form)


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    success_url = '/greenhouse/plants/'
    form_class = PlantForm

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Plant.objects.filter(owner=self.request.user)
        else:
            return Plant.objects.none()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return FormMixin.form_valid(self, form)


class PlantDetailView(LoginRequiredMixin, DetailView):
    model = Plant

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Plant.objects.filter(owner=self.request.user)
        else:
            return Plant.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_url'] = self.request.build_absolute_uri()
        context['control_list'] = Control.objects.filter(plant__slug=self.kwargs['slug']).order_by('-capture_date')
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        format_response = self.request.GET.get('format', '')
        if format_response == 'json':
            return JsonResponse({
                'object_url': context['object_url'],
                'object': model_to_dict(self.object),
                'control_list': list(context['control_list'].values()),
            })
        return self.render_to_response(context)


class ControlCreateView(LoginRequiredMixin, CreateView):
    model = Control
    success_url = '/greenhouse/plants/'
    form_class = ControlForm

    def form_valid(self, form):
        
        # Comprobacion si la planta me pertenece
        plant = Plant.objects.filter(slug=self.kwargs['slug'], owner=self.request.user)

        if len(plant) == 1:
            self.object = form.save(commit=False)
            self.object.plant = plant.get()

            if self.object.capture_date is None:
                self.object.capture_date = timezone.now()

            self.object.save()
            return FormMixin.form_valid(self, form)
        return HttpResponse('Unauthorized', status=401)