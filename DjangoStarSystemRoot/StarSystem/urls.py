from django.urls import path
from .views import (
    GalaxyListView, GalaxyCreateView, GalaxyDetailView,
    PlanetListView, PlanetCreateView, PlanetDetailView,
    StarListView, StarCreateView, StarDetailView,
    StarSystemCreateView, StarSystemDetailView, StarSystemListView
)

urlpatterns = [
    path('galaxy/', GalaxyListView.as_view(), name='galaxy-list'),
    path('galaxy/create', GalaxyCreateView.as_view(), name='galaxy-create'),
    path('galaxy/<int:pk>', GalaxyDetailView.as_view(), name='galaxy-detail'),
    path('planet/', PlanetListView.as_view(), name='planet-list'),
    path('planet/create', PlanetCreateView.as_view(), name='planet-create'),
    path('planet/<int:pk>', PlanetDetailView.as_view(), name='planet-detail'),
    path('star/', StarListView.as_view(), name='star-list'),
    path('star/create', StarCreateView.as_view(), name='star-create'),
    path('star/<int:pk>', StarDetailView.as_view(), name='star-detail'),
    path('star_system/', StarSystemListView.as_view(), name='star-system-list'),
    path('star_system/create', StarSystemCreateView.as_view(), name='star-system-create'),
    path('star_system/<int:pk>', StarSystemDetailView.as_view(), name='star-system-detail'),
]