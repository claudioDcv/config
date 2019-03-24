from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
import json
from django.http import HttpResponse

from .models import Solution, ElementSolution
from .forms import ElementSolutionForm, SolutionForm


class SolutionListView(LoginRequiredMixin, ListView):
    model = Solution

    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class SolutionDetailView(LoginRequiredMixin, DetailView):
    model = Solution

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Solution.objects.filter(owner=self.request.user)
        else:
            return Solution.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_url'] = self.request.build_absolute_uri()
        context['element_list'] = ElementSolution.objects.filter(solution__pk=self.kwargs['pk']).order_by('label')
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class SolutionUpdateView(LoginRequiredMixin, UpdateView):
    model = Solution
    success_url = '/lab/solutions/'
    form_class = SolutionForm

    def get_success_url(self):
        return '/lab/solutions/detail/' + str(self.object.pk) + '/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Solution.objects.filter(owner=self.request.user)
        else:
            return Solution.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elementsolution_list'] = ElementSolution.objects.filter(owner=self.request.user)
        context['o_es'] = [item.pk for item in self.object.elements_solution.all()]
        context['object'] = self.object
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        
        elements_solution_list = self.request.POST.getlist('elements_solution')
        es_list = ElementSolution.objects.filter(
            owner=self.object.owner,
            pk__in=elements_solution_list
        )

        # limpiamos todas las soluciones
        self.object.elements_solution.clear()
        # recorremos y reasignamos
        for es in es_list:
            self.object.elements_solution.add(es)

        
        # self.object.plant_type = PlantType.objects.get(pk=self.request.POST.get('plant_type'))
        # self.object.group = Group.objects.get(pk=self.request.POST.get('group'))
        self.object.save()
        return FormMixin.form_valid(self, form)


class ElementSolutionListView(LoginRequiredMixin, ListView):
    model = ElementSolution

    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
    
    # http://localhost:8000/lab/elements-solution/?format=json
    def get(self, request, *args, **kwargs):
        format_response = self.request.GET.get('format', '')
        # sub_type = self.request.GET.get('sub_type', '')
        q_label = self.request.GET.get('q_label', '')
        
        # and sub_type is not None
        if format_response == 'json' and q_label is not None:
            qs = None
            if q_label:
                qs = self.get_queryset().filter(
                label__icontains=q_label).order_by(
                'label')[:100]
            else:
                qs = self.get_queryset().filter().order_by(
                'label')[:100]

            qs_json = json.dumps([dict(item) for item in qs.values('label', 'pk')])

            return HttpResponse(qs_json, content_type='application/json')
        # JSON JSON
        return super(ElementSolutionListView, self).get(request, *args, **kwargs)


class ElementSolutionUpdateView(LoginRequiredMixin, UpdateView):
    model = ElementSolution
    success_url = '/lab/elements-solution/'
    form_class = ElementSolutionForm

    def get_success_url(self):
        return '/lab/elements-solution/detail/' + str(self.object.pk) + '/'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ElementSolution.objects.filter(owner=self.request.user)
        else:
            return ElementSolution.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        # self.object.plant_type = PlantType.objects.get(pk=self.request.POST.get('plant_type'))
        # self.object.group = Group.objects.get(pk=self.request.POST.get('group'))
        self.object.save()
        return FormMixin.form_valid(self, form)