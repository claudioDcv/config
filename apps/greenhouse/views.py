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
from django.core.paginator import Paginator

from .models import Plant, Control, PlantType, Group
from .forms import PlantForm, ControlForm, GroupForm

class PlantListView(LoginRequiredMixin, ListView):
    model = Plant

    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    success_url = '/greenhouse/plants/'
    form_class = PlantForm

    def get_success_url(self):
        return '/greenhouse/plants/detail/' + str(self.object.pk) + '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        self.object.plant_type = PlantType.objects.get(pk=self.request.POST.get('plant_type'))
        self.object.save()
        return FormMixin.form_valid(self, form)


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    success_url = '/greenhouse/plants/'
    form_class = PlantForm

    def get_success_url(self):
        return '/greenhouse/plants/detail/' + str(self.object.pk) + '/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Plant.objects.filter(owner=self.request.user)
        else:
            return Plant.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        self.object.plant_type = PlantType.objects.get(pk=self.request.POST.get('plant_type'))
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
        context['control_list'] = Control.objects.filter(plant__pk=self.kwargs['pk']).order_by('-capture_date')
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

    def get_success_url(self):
        return '/greenhouse/controls/update/' + str(self.object.plant.pk) + '/'

    def form_valid(self, form):
        
        # Comprobacion si la planta me pertenece
        plant = Plant.objects.filter(pk=self.kwargs['pk'], owner=self.request.user)

        if len(plant) == 1:
            self.object = form.save(commit=False)
            self.object.plant = plant.get()

            if self.object.capture_date is None:
                self.object.capture_date = timezone.now()

            self.object.save()
            return FormMixin.form_valid(self, form)
        return HttpResponse('Unauthorized', status=401)


class ControlUpdateView(LoginRequiredMixin, UpdateView):
    model = Control
    success_url = '/greenhouse/plants/'
    form_class = ControlForm

    def get_success_url(self):
        return '/greenhouse/plants/detail/' + str(self.object.plant.pk) + '/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Control.objects.filter(plant__owner=self.request.user)
        else:
            return Control.objects.none()

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context
    '''

    '''
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        self.object.plant_type = PlantType.objects.get(pk=self.request.POST.get('plant_type'))
        self.object.save()
        return FormMixin.form_valid(self, form)
    '''

class PlantTypeView(LoginRequiredMixin, ListView):
    model = PlantType

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # se agrega la lista del sistema + lista del usuario
            return PlantType.objects.filter(owner__in=[2, self.request.user])
        else:
            return PlantType.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    # http://localhost:8000/greenhouse/plant-types/
    # ?format=json&sub_type=Sativa%20(dominant)
    # ?format=json&q_label=Afrodite
    def get(self, request, *args, **kwargs):
        format_response = self.request.GET.get('format', '')
        # sub_type = self.request.GET.get('sub_type', '')
        q_label = self.request.GET.get('q_label', '')
        
        # and sub_type is not None
        if format_response == 'json' and q_label is not None:
            qs = self.get_queryset().filter(
                label__icontains=q_label).order_by(
                'label')[:100]
                # .filter(sub_type=sub_type)

            qs_json = json.dumps([dict(item) for item in qs.values('label', 'pk', 'sub_type')])

            return HttpResponse(qs_json, content_type='application/json')
        return HttpResponse([], content_type='application/json')


class GroupListView(LoginRequiredMixin, ListView):
    model = Group

    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    success_url = '/greenhouse/groups/'
    form_class = GroupForm

    def get_success_url(self):
        return '/greenhouse/groups/update/' + str(self.object.pk) + '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return FormMixin.form_valid(self, form)


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    success_url = '/greenhouse/groups/'
    form_class = GroupForm

    def get_success_url(self):
        return '/greenhouse/groups/detail/' + str(self.object.pk) + '/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Group.objects.filter(owner=self.request.user)
        else:
            return Group.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        self.object.save()
        return FormMixin.form_valid(self, form)


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Group.objects.filter(owner=self.request.user)
        else:
            return Group.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_url'] = self.request.build_absolute_uri()
        context['plant_list'] = Plant.objects.filter(group__pk=self.kwargs['pk'])
        # .order_by('-capture_date')
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