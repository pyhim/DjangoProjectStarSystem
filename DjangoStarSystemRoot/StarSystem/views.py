from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Galaxy, StarSystem, Star, Planet
from .forms import GalaxyForm, StarSystemForm, StarForm, PlanetForm

# Create your views here.


class GalaxyListView(ListView):
    template_name = 'galaxy_list.html'

    model = Galaxy
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'List of galaxies',
            'list_len': len(context['galaxy_list'])
        })
        return context


class GalaxyDetailView(DetailView):
    template_name = 'galaxy.html'
    model = Galaxy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalaxyCreateView(CreateView):
    template_name = 'galaxy_create.html'

    model = Galaxy
    form_class = GalaxyForm


class StarSystemListView(ListView):
    template_name = 'starsystem_list.html'

    model = StarSystem
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'List of star systems',
            'list_len': len(context['starsystem_list'])
        })
        return context


class StarSystemDetailView(DetailView):
    template_name = 'starsystem.html'
    model = StarSystem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StarSystemCreateView(CreateView):
    template_name = 'starsystem_create.html'

    model = StarSystem
    form_class = StarSystemForm


class StarListView(ListView):
    template_name = 'star_list.html'

    model = Star
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'List of stars',
            'list_len': len(context['star_list'])
        })
        return context


class StarDetailView(DetailView):
    template_name = 'star.html'
    model = Star

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StarCreateView(CreateView):
    template_name = 'star_create.html'

    model = Star
    form_class = StarForm


class PlanetListView(ListView):
    template_name = 'planet_list.html'

    model = Planet
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'List of planets',
            'list_len': len(context['planet_list'])
        })
        return context


class PlanetDetailView(DetailView):
    template_name = 'planet.html'
    model = Planet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PlanetCreateView(CreateView):
    template_name = 'planet_create.html'

    model = Planet
    form_class = PlanetForm
