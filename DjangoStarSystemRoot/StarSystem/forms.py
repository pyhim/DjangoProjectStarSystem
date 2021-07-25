from django import forms
from .models import Galaxy, StarSystem, Star, Planet

# Create your forms here


class GalaxyForm(forms.ModelForm):

    class Meta:
        model = Galaxy
        fields = '__all__'


class StarSystemForm(forms.ModelForm):
    class Meta:
        model = StarSystem
        fields = '__all__'


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = '__all__'


class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'
