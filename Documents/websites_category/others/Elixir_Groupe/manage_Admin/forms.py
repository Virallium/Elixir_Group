from django import forms
from .models import Evenements, Intervenants, Interview, Partenaires
from pages.models import Actualites, Opportunites, Publication

class Add_Evenements(forms.ModelForm):
    class Meta:
        model = Evenements
        fields = '__all__'

class Add_Actualites(forms.ModelForm):
    class Meta:
        model = Actualites
        fields ='__all__'

class Add_Intervenants(forms.ModelForm):
    class Meta:
        model = Intervenants
        fields = '__all__'

class Add_Publication(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class Add_Opportunites(forms.ModelForm):
    class Meta:
        model = Opportunites
        fields = '__all__'

class Add_Partenaires(forms.ModelForm):
    class Meta:
        model = Partenaires
        fields = '__all__'

class Add_Interview(forms.ModelForm):
    class Meta:
        model = Interview
        fields = '__all__'




